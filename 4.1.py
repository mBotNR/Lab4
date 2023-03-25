class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self, V):

        return Vector(self.x + V.x, self.y + V.y, self.z + V.z)

    def __sub__(self, V):

        return Vector(self.x - V.x, self.y - V.y, self.z -V.z)

    def __mul__(self, V):

        return Vector(self.y * V.z - self.z * V.y,
                      self.z * V.x - self.x * V.z,
                      self.x * V.y - self.y * V.x)
vec1 = Vector(1, 3, 6)
vec2 = Vector(2, 4, 1)
vec3 = vec1.__abs__(vec2)
printVec = '; '.join([str(vec3.x), str(vec3.y), str(vec3.z)])
print('(' + printVec + ')')
