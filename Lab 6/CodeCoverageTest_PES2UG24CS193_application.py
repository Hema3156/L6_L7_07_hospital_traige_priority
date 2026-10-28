
import pytest

from hospital_triage_priority import (
    process_triage_wards,
    monitor_oxygen_manifolds,
)


def test_invalid_wards_input():
    with pytest.raises(ValueError):
        process_triage_wards("invalid", 10)


def test_negative_default_acuity():
    with pytest.raises(ValueError):
        process_triage_wards([], -1)


def test_empty_wards():
    result = process_triage_wards([], 10)
    assert result == {
        "acuity_score": 0,
        "status": "NO_URGENT_CASES",
    }


def test_non_accepting_ward():
    wards = [{"is_accepting": False, "patients": []}]
    result = process_triage_wards(wards, 10)
    assert result["status"] == "NO_URGENT_CASES"


def test_default_ward_and_patient_values():
    wards = [{"is_accepting": True, "patients": [{}]}]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 10


def test_invalid_spo2_and_heart_rate():
    wards = [{
        "is_accepting": True,
        "patients": [
            {"spo2": 0, "hr": 75},
            {"spo2": 98, "hr": 0},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 0
    assert result["status"] == "NO_URGENT_CASES"


def test_unconscious_patient_in_general_ward():
    wards = [{
        "is_accepting": True,
        "tier": "general",
        "patients": [{"unconscious": True}],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 100


def test_unconscious_patient_in_outpatient_ward():
    wards = [{
        "is_accepting": True,
        "tier": "outpatient",
        "icu_standby": False,
        "patients": [
            {"unconscious": True},
            {"spo2": 80, "hr": 130},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 0
    assert result["status"] == "NO_URGENT_CASES"


def test_low_oxygen_level():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 85, "hr": 80}],
    }]
    assert process_triage_wards(wards, 10)["acuity_score"] == 60


def test_high_heart_rate():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 98, "hr": 130}],
    }]
    assert process_triage_wards(wards, 10)["acuity_score"] == 60


def test_icu_standby_adds_acuity():
    wards = [{
        "is_accepting": True,
        "icu_standby": True,
        "patients": [{"spo2": 98, "hr": 75}],
    }]
    assert process_triage_wards(wards, 10)["acuity_score"] == 35


def test_ward_alert_after_five_flagged_entries():
    wards = [{
        "is_accepting": True,
        "patients": [
            {"spo2": 0, "hr": 75},
            {"spo2": 0, "hr": 75},
            {"spo2": 0, "hr": 75},
            {"spo2": 0, "hr": 75},
            {"spo2": 0, "hr": 75},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result["status"] == "WARD_ALERT"


def test_no_oxygen_sensor_data():
    assert monitor_oxygen_manifolds([]) == "NO_DATA"


def test_two_consecutive_low_pressure_readings():
    assert monitor_oxygen_manifolds([[3.5, 3.0]]) == "PRESSURE_FAILURE"


def test_normal_pressure_resets_low_streak():
    assert monitor_oxygen_manifolds([[3.5, 4.5, 3.0]]) == "PRESSURE_NORMAL"


def test_pressure_normal():
    assert monitor_oxygen_manifolds([[5.0, 4.5, 4.0]]) == "PRESSURE_NORMAL"


def test_failure_in_later_manifold():
    assert monitor_oxygen_manifolds([
        [5.0, 4.5],
        [3.0, 3.5],
    ]) == "PRESSURE_FAILURE"
