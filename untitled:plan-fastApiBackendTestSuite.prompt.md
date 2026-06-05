## Plan: FastAPI Backend Test Suite

Add a new top-level tests directory with pytest-based FastAPI tests focused on core API behavior (activities retrieval, signup, unregister), using isolated in-memory state per test to avoid cross-test pollution.

**Steps**
1. Update `/workspaces/skills-getting-started-with-github-copilot/requirements.txt` to include `pytest` so the test runner is installed with project dependencies.
2. Create baseline test package structure under `/workspaces/skills-getting-started-with-github-copilot/tests` with `__init__.py`, `conftest.py`, and endpoint-focused test modules. Depends on step 1.
3. Add shared fixtures in `/workspaces/skills-getting-started-with-github-copilot/tests/conftest.py` for `TestClient` and deterministic reset of `src.app.activities` before each test using a deep copy snapshot; this step blocks endpoint tests.
4. Implement core read endpoint tests in `/workspaces/skills-getting-started-with-github-copilot/tests/test_endpoints.py` for `GET /activities` response status and data shape/content expectations, and structure each test explicitly using AAA (Arrange, Act, Assert) comment sections. Depends on step 3.
5. Implement signup tests in `/workspaces/skills-getting-started-with-github-copilot/tests/test_signup.py` covering success (200), duplicate signup (400), and unknown activity (404), with AAA structure in every test and fixture usage concentrated in Arrange blocks. Depends on step 3, parallel with step 6.
6. Implement unregister tests in `/workspaces/skills-getting-started-with-github-copilot/tests/test_unregister.py` covering success (200), participant not enrolled (404), and unknown activity (404), following the same AAA structure and naming consistency. Depends on step 3, parallel with step 5.
7. Verify tests via pytest execution from repo root and confirm isolation by ensuring order-independent pass outcomes, while checking each test file consistently follows AAA formatting.

**Relevant files**
- `/workspaces/skills-getting-started-with-github-copilot/src/app.py` — source of route behavior, status codes, and in-memory `activities` state to mirror in assertions and fixture resets.
- `/workspaces/skills-getting-started-with-github-copilot/pytest.ini` — existing pytest configuration (`pythonpath = .`) that supports imports from `src`.
- `/workspaces/skills-getting-started-with-github-copilot/requirements.txt` — add `pytest` as the required test runner dependency alongside existing packages.
- `/workspaces/skills-getting-started-with-github-copilot/tests/conftest.py` — new shared fixtures for client/state setup.
- `/workspaces/skills-getting-started-with-github-copilot/tests/test_endpoints.py` — new tests for `GET /activities`.
- `/workspaces/skills-getting-started-with-github-copilot/tests/test_signup.py` — new tests for `POST /activities/{activity_name}/signup`.
- `/workspaces/skills-getting-started-with-github-copilot/tests/test_unregister.py` — new tests for `DELETE /activities/{activity_name}/signup`.

**Verification**
1. Run `pytest -q` from `/workspaces/skills-getting-started-with-github-copilot` and confirm all tests pass.
2. Run an individual module command such as `pytest -q tests/test_signup.py` to verify modular independence.
3. Re-run full suite twice consecutively (`pytest -q && pytest -q`) to validate state reset reliability.

**Decisions**
- Included scope: core API behavior only (as requested), focused on `/activities` read and signup/unregister lifecycle.
- Excluded scope: root redirect/static-file route tests, max-participant capacity behavior, and additional edge-case/contract tests.
- Assumption: current status-code behavior in `src/app.py` is intended and should be captured as-is.

**Further Considerations**
1. If you want to expand after baseline, next best addition is redirect/static route checks because they are low effort and improve smoke coverage.
2. If business rules change, add capacity enforcement tests after max-participant validation exists in backend logic.