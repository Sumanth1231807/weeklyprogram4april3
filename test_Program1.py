import pytest
import Program1

@pytest.mark.xfail
@pytest.mark.parametrize("x,result",[(8,4.0),(7,7.0),(8,7)])
def test_square_root(x,result):
    sqrt=Program1.square_root(x)
    assert sqrt == result

@pytest.mark.skip(reason="no need")
@pytest.mark.parametrize("a,b,c,result",[(4,3,8,7)])
def test_quadratic_equation(a,b,c,result):
    quatreq=Program1.quadratic_equation(a,b,c)
    assert quatreq == result

@pytest.mark.parametrize("celsius,result",[(7,37.8),(8,36.0)])
def test_cels_to_farh(celsius,result):
    cel=Program1.cels_to_farh(celsius)
    assert cel == result

@pytest.fixture
def input():
    x=14
    return x
def test_pos_neg_zero(input):
    result=Program1.pos_neg_zero(input)
    assert result == "positive"

@pytest.mark.parametrize("num,result",[(18,138),(8,100)])
def test_natural_num(num,result):
    natnum=Program1.natural_num(num)
    assert natnum == result