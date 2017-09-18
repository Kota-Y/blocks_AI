import numpy as np

a0 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
a1 = a0
a2 = a0
a3 = a0
a4 = a0
a5 = a0
a6 = a0
a7 = a0

ex_pieces=[a0]
#ex_pieces.append(a1)
#ex_pieces.append(a2)
#ex_pieces.append(a3)
#ex_pieces.append(a4)
#ex_pieces.append(a5)
#ex_pieces.append(a6)
#ex_pieces.append(a7)


b0 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
b1 = b0
b2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
b3 = b2
b4 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
b5 = b4
b6 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
b7 = b6

ex_pieces.append(b0)
#ex_pieces.append(b1)
ex_pieces.append(b2)
#ex_pieces.append(b3)
ex_pieces.append(b4)
#ex_pieces.append(b5)
ex_pieces.append(b6)
#ex_pieces.append(b7)


c0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
c1 = c0
c2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
c3 = c2
c4 = c0
c5 = c0
c6 = c2
c7 = c2

ex_pieces.append(c0)
#ex_pieces.append(c1)
ex_pieces.append(c2)
#ex_pieces.append(c3)
#ex_pieces.append(c4)
#ex_pieces.append(c5)
#ex_pieces.append(c6)
#ex_pieces.append(c7)


d0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
d1 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
d2 = d1
d3 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
d4 = d3
d5 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
d6 = d5
d7 = d0

#ex_pieces.append(d0)
ex_pieces.append(d1)
#ex_pieces.append(d2)
ex_pieces.append(d3)
#ex_pieces.append(d4)
ex_pieces.append(d5)
#ex_pieces.append(d6)
ex_pieces.append(d7)


e0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
e1 = e0
e2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
e3 = e2
e4 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
e5 = e4
e6 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
e7 = e6

ex_pieces.append(e0)
#ex_pieces.append(e1)
ex_pieces.append(e2)
#ex_pieces.append(e3)
ex_pieces.append(e4)
#ex_pieces.append(e5)
ex_pieces.append(e6)
#ex_pieces.append(e7)


f0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0]])
f1 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
f2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
f3 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
f4 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
f5 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
f6 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
f7 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0]])

ex_pieces.append(f0)
ex_pieces.append(f1)
ex_pieces.append(f2)
ex_pieces.append(f3)
ex_pieces.append(f4)
ex_pieces.append(f5)
ex_pieces.append(f6)
ex_pieces.append(f7)

g0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
g1 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
g2 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
g3 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
g4 = g1
g5 = g0
g6 = g3
g7 = g2

ex_pieces.append(g0)
ex_pieces.append(g1)
ex_pieces.append(g2)
ex_pieces.append(g3)
#ex_pieces.append(g4)
#ex_pieces.append(g5)
#ex_pieces.append(g6)
#ex_pieces.append(g7)


h0 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,0]])
h1 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,0,0,0,0]])
h2 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
h3 = h0
h4 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
h5 = h2
h6 = h1
h7 = h4

ex_pieces.append(h0)
#ex_pieces.append(h1)
ex_pieces.append(h2)
#ex_pieces.append(h3)
ex_pieces.append(h4)
#ex_pieces.append(h5)
ex_pieces.append(h6)
#ex_pieces.append(h7)


i0 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
i1 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0]])
i2 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
i3 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
i4 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
i5 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
i6 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]])
i7 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])

ex_pieces.append(i0)
ex_pieces.append(i1)
ex_pieces.append(i2)
ex_pieces.append(i3)
ex_pieces.append(i4)
ex_pieces.append(i5)
ex_pieces.append(i6)
ex_pieces.append(i7)

j0 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
j1 = j0
j2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
j3 = j2
j4 = j0
j5 = j0
j6 = j2
j7 = j2

ex_pieces.append(j0)
#ex_pieces.append(j1)
ex_pieces.append(j2)
#ex_pieces.append(j3)
#ex_pieces.append(j4)
#ex_pieces.append(j5)
#ex_pieces.append(j6)
#ex_pieces.append(j7)


k0 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0]])
k1 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
k2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
k3 = np.array([[0,0,0,0,0],[0,0,0,1,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
k4 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
k5 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
k6 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
k7 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,1],[0,1,0,0,0],[0,0,0,0,0]])

ex_pieces.append(k0)
ex_pieces.append(k1)
ex_pieces.append(k2)
ex_pieces.append(k3)
ex_pieces.append(k4)
ex_pieces.append(k5)
ex_pieces.append(k6)
ex_pieces.append(k7)


l0 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]])
l1 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
l2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
l3 = np.array([[0,0,0,0,0],[0,0,1,1,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
l4 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0]])
l5 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
l6 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
l7 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,1],[0,1,1,0,0],[0,0,0,0,0]])

ex_pieces.append(l0)
ex_pieces.append(l1)
ex_pieces.append(l2)
ex_pieces.append(l3)
ex_pieces.append(l4)
ex_pieces.append(l5)
ex_pieces.append(l6)
ex_pieces.append(l7)


m0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,0,0,0,0]])
m1 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,0,0,0]])
m2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,0,1,1,0],[0,0,0,0,0]])
m3 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
m4 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
m5 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
m6 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
m7 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,1,1,0,0],[0,0,0,0,0]])

ex_pieces.append(m0)
ex_pieces.append(m1)
ex_pieces.append(m2)
ex_pieces.append(m3)
ex_pieces.append(m4)
ex_pieces.append(m5)
ex_pieces.append(m6)
ex_pieces.append(m7)


n0 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0]])
n1 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
n2 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,0],[0,1,0,1,0],[0,0,0,0,0]])
n3 = np.array([[0,0,0,0,0],[0,1,0,1,0],[0,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])
n4 = n1
n5 = n0
n6 = n3
n7 = n2

ex_pieces.append(n0)
ex_pieces.append(n1)
ex_pieces.append(n2)
ex_pieces.append(n3)
#ex_pieces.append(n4)
#ex_pieces.append(n5)
#ex_pieces.append(n6)
#ex_pieces.append(n7)


o0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0]])
o1 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
o2 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
o3 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,1,1],[0,0,1,0,0],[0,0,0,0,0]])
o4 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
o5 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
o6 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
o7 = np.array([[0,0,0,0,0],[0,0,1,0,0],[1,1,1,1,0],[0,0,0,0,0],[0,0,0,0,0]])

ex_pieces.append(o0)
ex_pieces.append(o1)
ex_pieces.append(o2)
ex_pieces.append(o3)
ex_pieces.append(o4)
ex_pieces.append(o5)
ex_pieces.append(o6)
ex_pieces.append(o7)


p0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,0,0,0]])
p1 = p0
p2 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
p3 = p2
p4 = np.array([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
p5 = p4
p6 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0]])
p7 = p6

ex_pieces.append(p0)
#ex_pieces.append(p1)
ex_pieces.append(p2)
#ex_pieces.append(p3)
ex_pieces.append(p4)
#ex_pieces.append(p5)
ex_pieces.append(p6)
#ex_pieces.append(p7)


q0 = np.array([[0,0,1,0,0],[0,0,1,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,0]])
q1 = np.array([[0,0,1,0,0],[0,0,1,0,0],[1,1,1,0,0],[0,0,0,0,0],[0,0,0,0,0]])
q2 = q1
q3 = np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,0,0],[0,0,1,0,0],[0,0,1,0,0]])
q4 = q3
q5 = np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,1,1],[0,0,1,0,0],[0,0,1,0,0]])
q6 = q5
q7 = q0

#ex_pieces.append(q0)
ex_pieces.append(q1)
#ex_pieces.append(q2)
ex_pieces.append(q3)
#ex_pieces.append(q4)
ex_pieces.append(q5)
#ex_pieces.append(q6)
ex_pieces.append(q7)


r0 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
r1 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,1,0,0,0],[0,0,0,0,0]])
r2 = r1
r3 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
r4 = r3
r5 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0]])
r6 = r5
r7 = r0

#ex_pieces.append(r0)
ex_pieces.append(r1)
#ex_pieces.append(r2)
ex_pieces.append(r3)
#ex_pieces.append(r4)
ex_pieces.append(r5)
#ex_pieces.append(r6)
ex_pieces.append(r7)


s0 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
s1 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0]])
s2 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,0,0,0]])
s3 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])
s4 = s0
s5 = s1
s6 = s2
s7 = s3

ex_pieces.append(s0)
ex_pieces.append(s1)
ex_pieces.append(s2)
ex_pieces.append(s3)
#ex_pieces.append(s4)
#ex_pieces.append(s5)
#ex_pieces.append(s6)
#ex_pieces.append(s7)


t0 = np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
t1 = np.array([[0,0,0,0,0],[0,0,0,1,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
t2 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,0,0,0]])
t3 = np.array([[0,0,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
t4 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0]])
t5 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,1,0,0,0],[0,0,0,0,0]])
t6 = np.array([[0,0,0,0,0],[0,0,1,1,0],[0,1,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])
t7 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,0,0]])

ex_pieces.append(t0)
ex_pieces.append(t1)
ex_pieces.append(t2)
ex_pieces.append(t3)
ex_pieces.append(t4)
ex_pieces.append(t5)
ex_pieces.append(t6)
ex_pieces.append(t7)


u0 = np.array([[0,0,0,0,0],[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0],[0,0,0,0,0]])
u1 = u0
u2 = u0
u3 = u0
u4 = u0
u5 = u0
u6 = u0
u7 = u0

ex_pieces.append(u0)
#ex_pieces.append(u1)
#ex_pieces.append(u2)
#ex_pieces.append(u3)
#ex_pieces.append(u4)
#ex_pieces.append(u5)
#ex_pieces.append(u6)
#ex_pieces.append(u7)
