[default]
_default:
    @just --list

# Run all checks
check: test

# Run the tests
test *args:
    @uv run pytest {{args}}
