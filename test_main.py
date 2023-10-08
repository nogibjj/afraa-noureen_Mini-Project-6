"""
Test goes here

"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transfrom_load"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_update():
    """tests update"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "update",
            "1",
            "Butterscotch",
            "114",
            "7.5",
            "0.4",
            "25",
            "18",
            "2.2",
            "kids70g",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_delete():
    """tests delete"""
    result = subprocess.run(
        ["python", "main.py", "delete", "1"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_create():
    """tests create"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "create",
            "Butterscotch",
            "114",
            "7.5",
            "0.4",
            "25",
            "18",
            "2.2",
            "kids70g",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_run_query():
    """tests run_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "run_query",
            "SELECT * FROM baskin_icecream WHERE Flavour = 'Butterscotch'",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


def test_read():
    """tests read"""
    result = subprocess.run(
        ["python", "main.py", "read"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_create()
    test_read()
    test_update()
    test_delete()
    test_run_query()
