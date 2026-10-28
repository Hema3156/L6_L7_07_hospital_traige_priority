# L6_L7_07 — Hospital Triage Priority

## Lab 6: Code and Branch Coverage Analysis

### About
This project tests a Python module that evaluates hospital ward admission priority using patient vitals, consciousness level, ward capacity, and medical oxygen pressure readings.

The objective of this lab is to test the application and achieve at least 90% code coverage and branch coverage.

### Files

| File | Description |
|---|---|
| `hospital_triage_priority.py` | Application module being tested |
| `test_hospital_triage.py` | Starter test file |
| `CodeCoverageTest_PES2UG24CS193_application.py` | Test cases for code coverage |
| `BranchCoverageTest_PES2UG24CS193_application.py` | Test cases for branch coverage |
| `CodeCoverage_Result.png` | Screenshot of code coverage results |
| `BranchCoverage_Result.png` | Screenshot of branch coverage results |

### Tools Used
- Python
- Pytest
- Coverage.py

### How to Run the Tests

Run these commands from the `Lab 6` folder.

**1. Code coverage**

```bash
python3 -m pytest -v CodeCoverageTest_PES2UG24CS193_application.py
```

To measure code coverage:

```bash
python3 -m coverage erase
python3 -m coverage run --source=hospital_triage_priority -m pytest CodeCoverageTest_PES2UG24CS193_application.py
python3 -m coverage report -m
```

**2. Branch coverage**

```bash
python3 -m pytest -v BranchCoverageTest_PES2UG24CS193_application.py
```

To measure branch coverage:

```bash
python3 -m coverage erase
python3 -m coverage run --branch --source=hospital_triage_priority -m pytest BranchCoverageTest_PES2UG24CS193_application.py
python3 -m coverage report -m
```

### Results

| Measurement | Result |
|---|---|
| Code coverage test cases passed | 17 |
| Code coverage | 100% |
| Branch coverage test cases passed | 16 |
| Branch coverage | 100% |
| Statements covered | 45 out of 45 |
| Branches covered | 32 out of 32 |
| Partial branches | 0 |

Both code coverage and branch coverage exceed the required 90% target.

### Screenshots
- `CodeCoverage_Result.png` shows the code coverage results.
- `BranchCoverage_Result.png` shows the branch coverage results.

### Conclusion
The application was tested using separate code coverage and branch coverage test suites. All test cases passed, and both coverage measurements reached 100%.

