class Vector3D:
    """
    A call for 3D vector
    
    Arguments
    ---------
    x : float
        First number to be added
    y : float
        Second number to be added
    z : float
        Third number to be added
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, {self.z})"

    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):
        """Add two vectors"""
        if isinstance(other, (int, float)):
            return Vector3D(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"Cannot add Vector3D to object of type {type(other)}")

    def __eq__(self, other):
        """Return True if self == other"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        r"""Take the dot product btw this vector
        and another vector
        .. math:

            u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3 

        Parameter
        ---------
        other : Vector3D
            The vector to be dotted with
        
        Return
        ------
        float :
            The dot product
        """
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __mul__(self, other):
        return self.dot(other)
    
    def cross(self, other):
        """Take the dot product btw this vector
        and the other vector

        Parameter
        ---------
        other : Vector3D
            The vector to be cross with
        
        Return
        ------
        scalar Vector3D :
            The cross product
        """
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def __matmul__(self, other):
        return self.cross(other)


if __name__ == "__main__":
    v = Vector3D(1, 2, 3)
    u = 1
    w = v + u
    w == Vector3D(2, 3, 4)
