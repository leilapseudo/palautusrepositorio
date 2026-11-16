# Copilot instructions for this project

## Project overview

This repository contains a small Flask web app for a login/register flow. The implementation is intentionally simple and uses a layered structure rather than a database:

- `src/app.py` defines the HTTP routes and request handling.
- `src/services/user_service.py` contains the business rules for authentication and user creation.
- `src/repositories/user_repository.py` stores users in memory and handles lookup/creation/reset behavior.
- `src/entities/user.py` is the lightweight User model.
- `src/tests/` contains Robot Framework end-to-end tests that exercise the running app in a browser.
- `src/AppLibrary.py` gives the tests a convenience API for resetting the app state and creating seeded users.

The app runs on port 5001 and is designed to be tested against a live Flask server, not as a pure unit-test project.

## Commands

Use the project-local virtual environment in `.venv` rather than a globally installed Python.

### Run the app

```bash
cd C:/Users/leila/palautusrepositorio/viikko3/login
./.venv/bin/python src/index.py
```

The server listens on `http://localhost:5001`.

### Run the full test suite

```bash
cd C:/Users/leila/palautusrepositorio/viikko3/login
./.venv/bin/python -m robot src/tests
```

### Run a single test file

```bash
cd C:/Users/leila/palautusrepositorio/viikko3/login
./.venv/bin/python -m robot src/tests/login.robot
```

### Run one specific Robot test case

```bash
cd C:/Users/leila/palautusrepositorio/viikko3/login
./.venv/bin/python -m robot --test "Login With Correct Credentials" src/tests/login.robot
```

There is no dedicated lint command in this project; the main validation flow is the Robot suite.

## High-level architecture and code patterns

- The app is a classic Flask MVC-style split: routes in `app.py`, service logic in `services`, persistence in `repositories`, and the model in `entities`.
- User validation and credential checks belong in `UserService`; keep route handlers thin and focused on HTTP concerns such as reading form data and flashing messages.
- The repository is intentionally in-memory (`_users` list). Do not introduce persistence or a database unless the task explicitly requires it.
- Test setup resets application state through the `/tests/reset` endpoint; the Robot suite expects a live server and seeded data when needed.
- Exceptions are already used to signal validation/auth failures (`UserInputError` and `AuthenticationError`), and the route layer catches those exceptions and turns them into flashed error messages.

## Key conventions specific to this codebase

- Keep form field names as they are: `username`, `password`, and `password_confirmation`.
- Use the existing service/repository boundaries instead of bypassing them from route handlers.
- Prefer raising the domain-specific exceptions in `user_service.py` over returning ad hoc strings from validation logic.
- The project uses Robot Framework Browser tests with a browser-driven, end-to-end workflow against the live app. If you modify behavior, update the relevant `.robot` test file rather than adding a different testing style.
- The app is intentionally minimal; new feature work should fit the same layered pattern instead of scattering logic across routes.

## Working in this repo

- Keep changes small and aligned with the current structure: Flask route -> service -> repository -> in-memory entity.
- When adding new user-facing validation, mirror the same exception flow used by `check_credentials` and `create_user`.
- When verifying behavior, prefer the existing Robot tests over ad hoc scripts, because they match the project’s real browser-based workflow.
