import matplotlib.pyplot as plt
import numpy as np
#from skimage.measure import marching_cubes_lewiner
from skimage import measure 

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage.draw import ellipsoid


# mask is a currently stored binary 3D numpy array 
ellip_base = ellipsoid(2, 1, 5, levelset=True)
ellip_double = np.concatenate((ellip_base[:-1, ...], ellip_base[2:, ...]), axis=0) 
verts, faces, normals, values = measure.marching_cubes(ellip_double,0)
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="3d")

ax.set_xlim(np.min(verts[:,0]), np.max(verts[:,0]))
ax.set_ylim(np.min(verts[:,1]), np.max(verts[:,1])) 
ax.set_zlim(np.min(verts[:,2]), np.max(verts[:,2]))

mesh = Poly3DCollection(verts[faces])
mesh.set_edgecolor('k')
ax.add_collection3d(mesh)
plt.tight_layout()
plt.show()