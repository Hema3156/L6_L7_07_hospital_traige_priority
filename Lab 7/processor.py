
import math


def parse_vitals_summary(vitals_csv):
    try:
        if not isinstance(vitals_csv, str):
            return "Invalid vitals input"

        parts = vitals_csv.strip().split(',')

        if len(parts) != 3:
            return "Invalid vitals input"

        hr = float(parts[0])
        spo2 = float(parts[1])
        temp = float(parts[2])

        if not all(math.isfinite(x) for x in (hr, spo2, temp)):
            return "Invalid vitals input"

        critical = hr > 120 or spo2 < 90 or temp > 39.0

        return (
            f"Vitals: HR={hr}, SpO2={spo2}% - "
            f"{'CRITICAL' if critical else 'STABLE'}"
        )

    except (ValueError, TypeError):
        return "Invalid vitals input"


def compute_patient_bmi(bmi_string):
    try:
        if not isinstance(bmi_string, str):
            return None

        parts = bmi_string.strip().split('/')

        if len(parts) != 2:
            return None

        weight = float(parts[0])
        height = float(parts[1])

        if not math.isfinite(weight) or not math.isfinite(height):
            return None

        if weight <= 0 or height <= 0:
            return None

        bmi = weight / (height ** 2)

        return round(bmi, 2)

    except (ValueError, TypeError, OverflowError):
        return None


def assign_ward_bed(allocation_code):
    try:
        if not isinstance(allocation_code, str):
            return "Invalid allocation code"

        parts = allocation_code.strip().split('-')

        if len(parts) != 2:
            return "Invalid allocation code"

        ward, bed_str = parts

        ward_names = {
            "ER": "Emergency Room",
            "ICU": "Intensive Care Unit",
            "GEN": "General Ward",
            "PED": "Pediatrics"
        }

        ward = ward.strip().upper()
        bed_str = bed_str.strip()

        if ward not in ward_names:
            return "Invalid allocation code"

        bed_num = int(bed_str)

        if bed_num <= 0:
            return "Invalid allocation code"

        return f"{ward_names[ward]} Bed #{bed_num}"

    except (ValueError, TypeError):
        return "Invalid allocation code"


def main():
    print("==== Running parse_vitals_summary ====")
    v_input = input("Enter vitals (HR,SpO2,Temp): ")
    print("Summary:", parse_vitals_summary(v_input))

    print("\n==== Running compute_patient_bmi ====")
    b_input = input("Enter weight/height (e.g. 70/1.75): ")
    print("BMI:", compute_patient_bmi(b_input))

    print("\n==== Running assign_ward_bed ====")
    w_input = input("Enter allocation (e.g. ICU-05): ")
    print("Assignment:", assign_ward_bed(w_input))


if __name__ == "__main__":
    main()

