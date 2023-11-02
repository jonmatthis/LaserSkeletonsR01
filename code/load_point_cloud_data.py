import numpy as np
import open3d as o3d
import pyvista as pv
from scipy.spatial import Delaunay

# Load the data from the .csv file
data = np.genfromtxt(r"C:\Users\jonma\Downloads\s8_18_pupilShadowMesh.csv", delimiter=',')

print(f"Original data size - {data.size}")
# Clear NaNs and Infs
data = data[~np.isnan(data).any(axis=1)]
data = data[~np.isinf(data).any(axis=1)]
print(f" data size  after removing nan and inf - {data.size}")

# Convert to Open3D format
print("Convert dottos to point cloud")
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(data)

# Save as a .pcd file
o3d.io.write_point_cloud("output.pcd", pcd)


print("Perform Delaunay triangulation...")

tri = Delaunay(data)

print("Convert to PyVista mesh object...")
mesh = pv.PolyData(data, tri.simplices)

print("Save as .stl...")
mesh.save("output.stl")