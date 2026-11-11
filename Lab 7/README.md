# Lab 7 – Fuzz Testing with Hypothesis
## Hospital Triage Priority System

### 1. Overview

This lab demonstrates how fuzz testing can be used to identify and fix input validation bugs in a Hospital Triage Priority System.

The application contains three functions that process patient and hospital allocation data:

- `parse_vitals_summary()` – Processes patient vital signs.
- `compute_patient_bmi()` – Calculates a patient's Body Mass Index (BMI).
- `assign_ward_bed()` – Assigns a patient to a hospital ward and bed.

Initially, these functions did not handle malformed or unexpected inputs safely. Hypothesis was used to generate different inputs and identify cases that caused the application to crash.

### 2. Objectives

- Understand the concept of fuzz testing.
- Use Hypothesis to generate a variety of test inputs.
- Identify input validation and exception-handling bugs.
- Fix the identified bugs in the application.
- Verify that the application handles invalid inputs safely.
- Ensure that valid inputs continue to produce the expected results.

### 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Application development |
| pytest | Running automated tests |
| Hypothesis | Property-based and fuzz testing |
| VS Code | Code editing |
| macOS Terminal | Executing the application and tests |

### 4. Project Structure

```text
Lab 7/
│
├── README.md
├── processor.py
└── test_processor.py
```

### 5. Application Functions

**5.1 parse_vitals_summary(vitals_csv)**

- Accepts patient vital signs in the format `HR,SpO2,Temperature`.
- Converts the values into floating-point numbers.
- Checks whether the patient's readings indicate a critical condition.
- Returns a summary with either `CRITICAL` or `STABLE`.
- Handles invalid input safely.

Example:

```python
parse_vitals_summary("75,98,37")
```

Expected output:

```text
Vitals: HR=75.0, SpO2=98.0% - STABLE
```

**5.2 compute_patient_bmi(bmi_string)**

- Accepts weight and height in the format `weight/height`.
- Converts both values into floating-point numbers.
- Calculates BMI using the formula:

\[
BMI = \frac{Weight\ (kg)}{Height\ (m)^2}
\]

- Rounds the result to two decimal places.
- Rejects invalid, non-positive, and non-finite values safely.

Example:

```python
compute_patient_bmi("70/1.75")
```

Expected output:

```text
22.86
```

**5.3 assign_ward_bed(allocation_code)**

- Accepts a hospital allocation code such as `ICU-05`.
- Identifies the ward and bed number.
- Supports the following ward codes:

| Code | Ward |
|---|---|
| ER | Emergency Room |
| ICU | Intensive Care Unit |
| GEN | General Ward |
| PED | Pediatrics |

- Validates the ward code and bed number.
- Returns an appropriate allocation message or an invalid-input message.

Example:

```python
assign_ward_bed("ICU-05")
```

Expected output:

```text
Intensive Care Unit Bed #5
```

### 6. Installation and Setup

**Step 1: Install the required dependencies.**

```bash
python3 -m pip install hypothesis pytest
```

**Step 2: Navigate to the Lab 7 directory.**

```bash
cd "Lab 7"
```

### 7. Fuzz Testing Using Hypothesis

Hypothesis is a Python library used for property-based testing. It automatically generates different inputs, including unexpected and invalid values, to identify potential bugs.

The test file uses the following imports:

```python
from hypothesis import given, strategies as st
from processor import (
    parse_vitals_summary,
    compute_patient_bmi,
    assign_ward_bed
)
```

The `@given` decorator allows Hypothesis to generate multiple test inputs automatically.

The strategy `st.text() | st.none()` generates text values as well as `None`.

Three tests were implemented:

1. `test_parse_vitals_summary_no_crash`
2. `test_compute_patient_bmi_safe`
3. `test_assign_ward_bed_safe`

Each test uses `try` and `except` to detect unexpected exceptions. If a function crashes, the test fails and reports the error.

### 8. Testing Procedure

**Step 1: Run the original application.**

```bash
python3 processor.py
```

Valid sample inputs were provided to verify the original application.

**Step 2: Run the initial Hypothesis tests.**

```bash
python3 -m pytest test_processor.py
```

The initial tests identified failures in all three functions.

Some examples of discovered issues included:

- Missing values causing `IndexError`.
- Invalid numeric values causing `ValueError`.
- `None` inputs causing `AttributeError`.
- Incorrect input formats causing unpacking errors.

**Step 3: Fix the application.**

The application was updated with input validation and exception handling.

The fixes include:

- Checking input data types.
- Validating the number of input fields.
- Handling invalid numeric conversions.
- Rejecting non-finite values such as `NaN` and infinity.
- Checking positive BMI inputs.
- Validating ward codes and bed numbers.
- Returning safe error values instead of allowing unexpected exceptions.

**Step 4: Verify the corrected application.**

```bash
python3 processor.py
```

The application was tested again using valid sample inputs.

**Step 5: Run Hypothesis tests again.**

```bash
python3 -m pytest test_processor.py
```

All three tests passed after the fixes were implemented.

### 9. Final Test Results

The final pytest execution produced the following result:

```text
collected 3 items

test_processor.py ... [100%]

3 passed in 0.28s
```

**Result:** All three Hypothesis tests passed successfully.

This confirms that the tested inputs did not cause unexpected exceptions in the corrected functions.

### 10. Conclusion

This lab demonstrated how fuzz testing with Hypothesis can identify input validation bugs that may not be discovered through ordinary testing.

Initially, all three functions failed when Hypothesis generated unexpected inputs. After implementing input validation and exception handling, the application handled the tested invalid inputs safely.

The final test execution completed successfully, with **3 out of 3 tests passing**.

### Deliverables

The following files are included in the Lab 7 submission:

1. `Lab_7_Fuzz_Testing_Screenshots.pdf` – PDF document containing screenshots of the original application output, initial failing Hypothesis tests, fixed application output, and final passing tests.

2. `processor.py` – Fixed application Python script with improved input validation and exception handling.

3. `test_processor.py` – Updated Hypothesis-based test code used to identify input validation bugs in all three functions.
