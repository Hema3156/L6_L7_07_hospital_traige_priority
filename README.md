# Hospital Triage Priority

## About the Project

This repository contains the implementation and testing work for Lab 6 and Lab 7 of the Hospital Triage Priority assignment.

The labs focus on software testing techniques used to evaluate application functionality, identify potential bugs, measure test coverage, and improve code reliability.

## Lab 6 – Code Coverage and Branch Coverage

Lab 6 focuses on testing the Hospital Triage Priority application using code coverage and branch coverage techniques.

The work includes:

- Implementing and testing the hospital triage priority application.
- Writing automated test cases using pytest.
- Measuring code coverage to identify executed and unexecuted lines.
- Evaluating branch coverage to check different decision paths.
- Generating coverage reports to analyse test effectiveness.

**Key files:** `hospital_triage_priority.py`, `test_hospital_triage.py`, and the coverage testing scripts.

## Lab 7 – Fuzzing for Input Validation Bugs

Lab 7 focuses on identifying and fixing input validation bugs using Hypothesis, a Python property-based testing library.

The work includes:

- Writing automated tests using Hypothesis.
- Generating random, unexpected, and malformed inputs.
- Identifying application crashes and edge cases.
- Improving input validation and exception handling.
- Re-running tests to verify the fixes.

The three Hypothesis tests passed successfully after the application was corrected.

**Key files:** `processor.py` and `test_processor.py`.

## Technologies Used

- **Python** – Application development and implementation.
- **pytest** – Automated testing.
- **Hypothesis** – Property-based fuzz testing.
- **Coverage.py** – Code and branch coverage analysis.
- **Git and GitHub** – Version control and project management.

## Repository Structure

```text
L6_L7_07_hospital_traige_priority/
│
├── Lab 6/
│   ├── hospital_triage_priority.py
│   ├── test_hospital_triage.py
│   ├── CodeCoverageTest_PES2UG24CS193_application.py
│   ├── BranchCoverageTest_PES2UG24CS193_application.py
│   ├── CodeCoverageTest.png
│   ├── BranchCoverageTest.png
│   ├── htmlcov/
│   └── README.md
│
├── Lab 7/
│   ├── processor.py
│   ├── test_processor.py
│   ├── Lab_7_Fuzz_Testing_Screenshots.pdf
│   ├── 01_Original_Processor_Output.png
│   ├── 02_Failing_Hypothesis_Tests p1.png
│   ├── 02_Failing_Hypothesis_Tests p2.png
│   ├── 02_Failing_Hypothesis_Tests p3.png
│   ├── 03_Fixed_Processor_Output.png
│   ├── 04_Passing_Hypothesis_Tests.png
│   └── README.md
│
└── README.md
```

## Learning Outcomes

- Understanding software testing techniques.
- Writing and executing automated test cases.
- Analysing code and branch coverage.
- Identifying unexpected input-related failures.
- Applying fuzz testing using Hypothesis.
- Improving application robustness through input validation and defensive programming.

## Documentation

Each lab folder contains its own README with the respective objectives, implementation details, testing procedure, and results.
