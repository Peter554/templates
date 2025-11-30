import subprocess

import copier


def test_template_py(tmp_path):
    copier.run_copy(
        "./py",
        tmp_path,
        data={
            "project_name": "foo",
            "project_slug": "foo",
            "description": "foo",
        },
    )

    assert (
        subprocess.run(["just", "check"], cwd=tmp_path, capture_output=True).returncode
        == 0
    )
