import numpy as np
from scipy.constants import mu_0, pi

from src.fields import VectorField


class BiotSavartEquationSolver:
    """
    A Biot–Savart law solver used to compute the resultant magnetic field B in 2D-space generated by a constant current
    field I (for example due to wires).
    """

    def solve(self, electric_current: VectorField) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (x, y) → (I_x(x, y), I_y(x, y), I_z(x, y)), where I_x(x, y), I_y(x, y) and
            I_z(x, y) are the 3 components of the electric current vector at a given point (x, y) in space. Note that
            I_z = 0 is always True in our 2D world.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (x, y) → (B_x(x, y), B_y(x, y), B_z(x, y)), where B_x(x, y), B_y(x, y) and
            B_z(x, y) are the 3 components of the magnetic vector at a given point (x, y) in space. Note that
            B_x = B_y = 0 is always True in our 2D world. 
        Developped by Émile Tremblay-Antoine and Xavier Arrata"""
        
        # Find all current vectors and their corresponding positions
        position, current = [], []
        for row, row_value in enumerate(electric_current):
            for column, cell in enumerate(row_value):
                # If a current exists at a given point, it is registered
                if cell[0] or cell[1] != 0:
                    position.append((row, column, 0))
                    current.append(cell)
        # Creates an array of zeros that has the dimensions of the electric current field
        magnetic_field = np.zeros(np.shape(electric_current))
        # Calculate cross product of current and r vector for each point in the magnetic field Vector Space
        for row, row_value in enumerate(magnetic_field):
            for column, cell in enumerate(row_value):
                if (row, column, 0) not in position:
                    # Calculate the r vector
                    r = np.array([row, column, 0]) - np.array(position)
                    # Compute the lenght of the r vector
                    r_norm = (np.linalg.norm(r, axis=1))**3
                    # Calculate the cross product between the position of the point of interest and the element of current
                    cross_product = np.cross(current, r)
                    # Calculate the magnetic field at the point of interest
                    magnetic_field[row, column] = [int(0),int(0),np.sum(mu_0 * cross_product[:,2] / (4 * pi * r_norm))]
        return VectorField(magnetic_field)
                    

        


