import sys
import unittest
import xml.etree.ElementTree as ET


# Discover tests
suite = unittest.defaultTestLoader.discover(
    start_dir="tests",
    pattern="test_*.py"
)


# Flatten the test suite BEFORE running it
def flatten(test_suite):
    tests = []

    for test in test_suite:
        if isinstance(test, unittest.TestSuite):
            tests.extend(flatten(test))
        else:
            tests.append(test)

    return tests


tests = flatten(suite)


# Run tests
result = unittest.TestResult()
suite.run(result)


# Store results
failures = dict(result.failures)
errors = dict(result.errors)
skipped = dict(result.skipped)


# Create JUnit-compatible XML
root = ET.Element(
    "testsuite",
    {
        "name": "Python Tests",
        "tests": str(result.testsRun),
        "failures": str(len(result.failures)),
        "errors": str(len(result.errors)),
        "skipped": str(len(result.skipped)),
    }
)


# Add each test case
for test in tests:
    testcase = ET.SubElement(
        root,
        "testcase",
        {
            "classname": (
                test.__class__.__module__
                + "."
                + test.__class__.__name__
            ),
            "name": test._testMethodName,
        }
    )

    if test in failures:
        ET.SubElement(
            testcase,
            "failure",
            {"message": "Test failure"}
        ).text = failures[test]

    elif test in errors:
        ET.SubElement(
            testcase,
            "error",
            {"message": "Test error"}
        ).text = errors[test]

    elif test in skipped:
        ET.SubElement(
            testcase,
            "skipped",
            {"message": skipped[test]}
        )


# Write XML report
ET.ElementTree(root).write(
    "test-results.xml",
    encoding="utf-8",
    xml_declaration=True
)


# Print summary
print(f"Tests run: {result.testsRun}")
print(f"Failures: {len(result.failures)}")
print(f"Errors: {len(result.errors)}")
print(f"Skipped: {len(result.skipped)}")


# Make Jenkins build fail if tests fail
if result.failures or result.errors:
    sys.exit(1)
