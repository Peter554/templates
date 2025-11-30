import subprocess

import copier


def test_template_py(tmp_path):
    copier.run_copy(
        "./templates/py",
        tmp_path,
        data={
            "project_name": "foo",
            "project_slug": "foo",
            "description": "foo",
            "python_version": "3.13",
            "create_cli": True,
            "git_init": False,
        },
        unsafe=True,
    )

    assert (
        subprocess.run(["just", "check"], cwd=tmp_path, capture_output=True).returncode
        == 0
    )
