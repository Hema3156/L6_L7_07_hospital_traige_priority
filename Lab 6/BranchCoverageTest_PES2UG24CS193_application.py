
import pytest

from hospital_triage_priority import (
    process_triage_wards,
    monitor_oxygen_manifolds,
)


def test_valid_and_invalid_input_branches():
    with pytest.raises(ValueError):
        process_triage_wards("invalid", 10)

    with pytest.raises(ValueError):
        process_triage_wards([], -1)

    assert process_triage_wards([], 10)["status"] == "NO_URGENT_CASES"


def test_accepting_and_non_accepting_wards():
    wards = [
        {"is_accepting": False, "patients": [{"spo2": 80, "hr": 130}]},
        {"is_accepting": True, "patients": [{"spo2": 98, "hr": 75}]},
    ]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 10


def test_default_values_and_empty_patient_list():
    wards = [
        {"is_accepting": True},
        {"is_accepting": True, "patients": [{}]},
    ]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 10


def test_invalid_spo2_and_invalid_heart_rate():
    wards = [{
        "is_accepting": True,
        "patients": [
            {"spo2": 0, "hr": 80},
            {"spo2": 95, "hr": 0},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 0


def test_unconscious_outpatient_stops_patient_processing():
    wards = [{
        "is_accepting": True,
        "tier": "outpatient",
        "patients": [
            {"unconscious": True},
            {"spo2": 80, "hr": 130},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result == {
        "acuity_score": 0,
        "status": "NO_URGENT_CASES",
    }


def test_unconscious_patient_in_other_ward():
    wards = [{
        "is_accepting": True,
        "tier": "general",
        "patients": [{"unconscious": True}],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 100


def test_low_spo2_branch():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 89, "hr": 100}],
    }]
    assert process_triage_wards(wards, 10)["acuity_score"] == 60


def test_high_heart_rate_branch():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 95, "hr": 121}],
    }]
    assert process_triage_wards(wards, 10)["acuity_score"] == 60


def test_normal_patient_branch():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 90, "hr": 120}],
    }]
    assert process_triage_wards(wards, 10)["acuity_score"] == 10


def test_icu_standby_enabled_and_disabled():
    wards = [
        {
            "is_accepting": True,
            "icu_standby": True,
            "patients": [{"spo2": 98, "hr": 75}],
        },
        {
            "is_accepting": True,
            "icu_standby": False,
            "patients": [{"spo2": 98, "hr": 75}],
        },
    ]
    assert process_triage_wards(wards, 10)["acuity_score"] == 45


def test_ward_alert_threshold():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 0, "hr": 75} for _ in range(5)],
    }]
    assert process_triage_wards(wards, 10)["status"] == "WARD_ALERT"


def test_pressure_no_data():
    assert monitor_oxygen_manifolds([]) == "NO_DATA"


def test_pressure_failure_on_second_low_reading():
    assert monitor_oxygen_manifolds([[3.0, 3.5]]) == "PRESSURE_FAILURE"


def test_normal_pressure_resets_streak():
    assert monitor_oxygen_manifolds([[3.0, 4.0, 3.5]]) == "PRESSURE_NORMAL"


def test_normal_and_empty_manifolds():
    assert monitor_oxygen_manifolds([[], [4.0, 5.0]]) == "PRESSURE_NORMAL"


def test_failure_in_second_manifold():
    assert monitor_oxygen_manifolds([[5.0], [3.0, 3.5]]) == "PRESSURE_FAILURE"
