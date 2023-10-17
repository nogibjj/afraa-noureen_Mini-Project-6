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


def test_run_query():
    """tests run_query"""
    result = subprocess.run(
        [
            "python",
            "main.py",
            "run_query",
            """SELECT Flavour, Sugars_g, Size 
            FROM BaskinRobbinsDB 
            WHERE Size = 'Reg114g' 
            ORDER BY Sugars_g DESC 
            LIMIT 5;
            """,
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_run_query()
