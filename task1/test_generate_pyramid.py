import pytest
from io import StringIO
from contextlib import redirect_stdout
from generate_pyramid import generate_pyramid

# Basic Valid cases
@pytest.mark.parametrize("height, char, expected_output", [
    (3, '*', "  *  \n *** \n*****\n"),
    (3, '#', "  #  \n ### \n#####\n"),
])
def test_generate_pyramid(height, char, expected_output):
    f = StringIO()
    with redirect_stdout(f):
        generate_pyramid(height, char)
    assert f.getvalue() == expected_output

# invalid heights
@pytest.mark.parametrize("height, char, expected_error", [
    (0, '', ValueError),
    (-1, 'A', ValueError),
    (21, 'A', ValueError),
    (3.14, 'A', TypeError),
])
def test_generate_pyramid_invalid_height(height, char, expected_error):
    with pytest.raises(expected_error):
        generate_pyramid(height, char)

# invalid characters
@pytest.mark.parametrize("height, char, expected_error", [
    (3, '##', ValueError),
    (20, '\'\'' , ValueError),
])
def test_generate_pyramid_invalid_char(height, char, expected_error):
    with pytest.raises(expected_error):
        generate_pyramid(height, char)

#Holistic test cases
def test_generate_pyramid_max_height():
    f = StringIO()
    with redirect_stdout(f):
        generate_pyramid(20)
    output_lines = f.getvalue().split('\n')
    assert len(output_lines) == 21  # 20 lines of pyramid + 1 empty line
    assert output_lines[0].strip() == '*'  # The first line has 1 asterisk
    assert len(output_lines[19].strip()) == 39  # The last line has 39 asterisks

def test_full_run():
    f = StringIO()
    with redirect_stdout(f):
        for i in range(1, 21):
            generate_pyramid(i)
    output = f.getvalue().split('\n')
    assert len(output) == 211  # 20 pyramids of height 1 to 20 + empty lines