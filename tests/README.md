# SvaraScala Test Suite

This directory contains the automated test suite for the SvaraScala library, which provides musical frequency calculations for both Western and Indian classical music systems.

## Test Structure

The tests are organized into the following modules:

- `test_init.py`: Tests for the package initialization
- `test_western.py`: Basic tests for Western music functionality
- `test_western_advanced.py`: Advanced tests for Western music functionality
- `test_indian.py`: Basic tests for Indian music functionality
- `test_indian_advanced.py`: Advanced tests for Indian music functionality
- `test_main.py`: Basic tests for the command-line interface
- `test_main_advanced.py`: Advanced tests for the command-line interface
- `test_suite.py`: A test suite runner that executes all tests

## Running Tests

### Using Test Suite Runner

To run all tests using the test suite runner:

```bash
python -m tests.test_suite
```

### Using pytest

To run tests using pytest with coverage reporting:

```bash
pytest
```

Pytest is configured in `pytest.ini` to automatically discover and run all tests, and generate coverage reports.

### Running Specific Test Modules

To run tests from a specific module:

```bash
python -m unittest tests.test_western
```

Or using pytest:

```bash
pytest tests/test_western.py
```

### Running Tests by Category

Using pytest markers:

```bash
pytest -m western  # Run Western music tests
pytest -m indian   # Run Indian music tests
pytest -m cli      # Run command-line interface tests
```

## Code Coverage

To generate a code coverage report:

```bash
pytest --cov=svarascala --cov-report=html
```

This will create an HTML coverage report in the `htmlcov` directory.

## Test Dependencies

The test suite requires the following dependencies:

- pytest
- pytest-cov
- pytest-mock
- coverage

You can install these dependencies using:

```bash
pip install -r requirements.txt
```

## Adding New Tests

When adding new tests, follow these guidelines:

1. Create test classes that inherit from `unittest.TestCase`
2. Name test methods with the prefix `test_`
3. Use descriptive method names that explain what is being tested
4. Add appropriate docstrings to test classes and methods
5. Keep tests focused on a single functionality or behavior
6. Add appropriate pytest markers for test categorization

## Fixtures

Common test fixtures are defined in `conftest.py`. These include:

- Various tuning instances for Western and Indian music
- Test data for parametrized tests
- Helper functions for common testing tasks

## Continuous Integration

The test suite is designed to be integrated with CI/CD pipelines. A sample workflow configuration is included in the repository.