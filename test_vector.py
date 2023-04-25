from vector import Vector3D
import pytest
import math

def test_vector_str():
    v = Vector3D(1, 2, 3)
    assert str(v) == '(1, 2, 3)'

def test_vector_repr():
    v = Vector3D(1, 2, 3)
    assert repr(v) == 'Vector3D(1, 2, 3)'

def test_vector_add():
    v = Vector3D(1, 2, 3)
    u = Vector3D(1, 1, 1)
    w = u + v
    assert w.x == 2
    assert w.y == 3
    assert w.z == 4

def test_vector_add_eq():
    v = Vector3D(1, 2, 3)
    u = Vector3D(1, 1, 1)
    w = u + v
    assert w == Vector3D(2, 3, 4)

def test_vector_add_integer():
    v = Vector3D(1, 2, 3)
    u = 1
    w = v + u
    assert w == Vector3D(2, 3, 4)

def test_vector_add_integer_right():
    v = Vector3D(1, 2, 3)
    u = 1
    w = u + v
    assert w == Vector3D(2, 3, 4)

def test_vector_add_string_raises_TypeError():
    v = Vector3D(1, 2, 3)
    u = "Hello"
    with pytest.raises(TypeError):
        u + v

def test_vector_dot_product():
    v = Vector3D(1, 2, 3)
    u = Vector3D(1, 1, 1)
    w = u.dot(v)
    assert isinstance(w, (int, float))
    #assert abs(w - 6) < 1e-12
    assert math.isclose(w, 6)

def test_vector_dot_product_mul():
    v = Vector3D(1, 2, 3)
    u = Vector3D(1, 1, 1)
    w = u * v
    assert isinstance(w, (int, float))
    #assert abs(w - 6) < 1e-12
    assert math.isclose(w, 6)

@pytest.mark.parametrize("u, v, expected", [(Vector3D(0, 1, 0), Vector3D(1, 0, 0), Vector3D(0, 0, -1))])
def test_vector_cross_product(u, v, expected):
    #v = Vector3D(1, 0, 0)
    #u = Vector3D(0, 1, 0)
    w = u.cross(v)
    assert w == expected #w == Vector3D(0, 0, -1)

@pytest.mark.parametrize("u, v, expected", [(Vector3D(0, 1, 0), Vector3D(1, 0, 0), Vector3D(0, 0, -1))])
def test_vector_cross_product(u, v, expected):
    w = u @ v
    assert w == expected
