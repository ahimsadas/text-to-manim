from manim import *
import numpy as np

class SpacetimeCurvature(Scene):
    def construct(self):
        # [0:00-0:08] Intro and title
        title = Text("Spacetime Curvature", font_size=60)
        title.to_edge(UP, buff=1)
        
        question = Text("?", font_size=100)
        question.shift(DOWN * 0.5)
        einstein_eq = MathTex(r"E=mc^2", font_size=80)
        einstein_eq.shift(DOWN * 0.5)
        
        self.play(Write(title), run_time=2)
        self.wait(0.5)
        self.play(FadeIn(question), run_time=1)
        self.play(Transform(question, einstein_eq), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(title), FadeOut(question), run_time=1)
        
        # [0:08-0:18] Transition from Newton to Einstein
        # Create a Newtonian gravity representation with plenty of space
        earth = Circle(radius=0.5, color=BLUE).shift(LEFT*4)
        sun = Circle(radius=1, color=YELLOW).shift(RIGHT*4)
        
        # Create force arrows with adequate spacing
        arrow1 = Arrow(earth.get_right(), sun.get_left(), buff=0.3, color=RED)
        arrow2 = Arrow(sun.get_left(), earth.get_right(), buff=0.3, color=RED)
        
        newton_group = VGroup(earth, sun, arrow1, arrow2)
        newton_group.move_to(ORIGIN)
        newton_group.scale(0.8)  # Scale down slightly to ensure screen fit
        
        self.play(Create(newton_group), run_time=2)
        
        # Cross out Newtonian concept
        cross = Cross(newton_group, stroke_width=6)
        self.play(Create(cross), run_time=1)
        self.wait(1)
        
        # Create spacetime grid
        grid = NumberPlane(
            x_range=(-8, 8, 1),
            y_range=(-4.5, 4.5, 1),
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        
        # Scale grid to leave room around edges
        grid.scale(0.9)
        
        self.play(
            FadeOut(newton_group), 
            FadeOut(cross),
            Create(grid),
            run_time=3
        )
        
        # [0:18-0:30] Show spacetime curvature
        # Function to create curved surface effect
        def curved_grid(grid_object, center, intensity=1):
            grid_copy = grid_object.copy()
            for mob in grid_copy.family_members_with_points():
                points = mob.get_points()
                for i, point in enumerate(points):
                    # Calculate distance from center
                    dist = np.linalg.norm(point[:2] - center[:2])
                    # Apply transformation (z-coordinate gets lower based on distance)
                    if dist < 3:
                        new_z = -intensity * max(0, (3 - dist)**2)
                        points[i][2] = new_z
            return grid_copy
        
        # Create a sun sphere
        sun = Sphere(radius=0.7, resolution=(20, 20))
        sun.set_color(YELLOW)
        sun.move_to(ORIGIN)
        
        # Create curved grid
        curve_center = np.array([0, 0, 0])
        curved_grid_obj = curved_grid(grid, curve_center, intensity=0.3)
        
        self.play(
            Transform(grid, curved_grid_obj),
            FadeIn(sun),
            run_time=4
        )
        
        # [0:30-0:40] Show planets following geodesics
        planets = VGroup()
        orbits = VGroup()
        
        # Create 3 planets at different distances with proper spacing
        for i, dist in enumerate([1.5, 2.3, 3.2]):
            planet = Sphere(radius=0.15, resolution=(10, 10))
            planet.set_color(BLUE)
            
            # Position planet
            angle = i * 2 * PI / 3
            position = np.array([dist * np.cos(angle), dist * np.sin(angle), -0.3 * (3 - dist)**2])
            planet.move_to(position)
            planets.add(planet)
            
            # Create orbit path
            orbit_points = []
            for theta in np.linspace(0, 2*PI, 100):
                x = dist * np.cos(theta)
                y = dist * np.sin(theta)
                z = -0.3 * (3 - np.sqrt(x**2 + y**2))**2 
                orbit_points.append([x, y, z])
            
            orbit = CurvesAsSubmobjects(VMobject().set_points_smoothly(orbit_points))
            orbit.set_color(BLUE_B)
            orbits.add(orbit)
        
        self.play(FadeIn(planets), run_time=2)
        self.play(Create(orbits), run_time=2)
        
        # Add geodesic label with proper spacing
        geodesic_label = Text("Geodesics", font_size=36)
        geodesic_label.to_edge(UP, buff=0.8)
        self.play(Write(geodesic_label), run_time=1)
        self.wait(3)
        self.play(FadeOut(geodesic_label), run_time=1)
        
        # [0:40-0:52] Split screen showing flat vs. curved geodesics
        self.play(
            FadeOut(planets),
            FadeOut(orbits),
            FadeOut(sun),
            FadeOut(grid),
            run_time=2
        )
        
        # Create a split screen with sufficient padding
        left_section = Rectangle(
            width=6, height=5, 
            stroke_width=0,
            fill_color=BLACK, 
            fill_opacity=0
        ).shift(LEFT * 3.5)
        
        right_section = Rectangle(
            width=6, height=5, 
            stroke_width=0,
            fill_color=BLACK, 
            fill_opacity=0
        ).shift(RIGHT * 3.5)
        
        # Left side: flat space
        flat_plane = NumberPlane(
            x_range=(-3, 3, 1),
            y_range=(-2, 2, 1)
        ).scale(0.4).move_to(left_section.get_center())
        
        flat_plane_center = flat_plane.get_center()
        point_a = Dot(flat_plane.c2p(-1.5, -1, 0), color=RED)
        point_b = Dot(flat_plane.c2p(1.5, 1, 0), color=RED)
        
        flat_line = Line(point_a.get_center(), point_b.get_center(), color=YELLOW)
        
        # Position the label with proper spacing
        flat_label = Text("Flat Space", font_size=24)
        flat_label.next_to(flat_plane, UP, buff=0.5)
        
        # Right side: curved space (sphere)
        sphere = Sphere(radius=1.3, resolution=(20, 20))
        sphere.set_color(BLUE_E).set_opacity(0.7)
        sphere.move_to(right_section.get_center())
        
        # Points on sphere
        sphere_center = sphere.get_center()
        sphere_point_a = Dot3D(sphere_center + np.array([-0.8, -0.7, 0.7]), color=RED)
        sphere_point_b = Dot3D(sphere_center + np.array([0.8, 0.7, 0.7]), color=RED)
        
        # Great circle path (approximation)
        great_circle_points = []
        start_point = sphere_point_a.get_center() - sphere_center
        end_point = sphere_point_b.get_center() - sphere_center
        
        # Normalize to lie on sphere
        start_norm = start_point / np.linalg.norm(start_point) * 1.3
        end_norm = end_point / np.linalg.norm(end_point) * 1.3
        
        # Generate points along great circle
        dot_product = np.dot(start_norm, end_norm) / (1.3**2)
        angle = np.arccos(np.clip(dot_product, -1.0, 1.0))
        
        for t in np.linspace(0, 1, 30):
            # Spherical interpolation (SLERP)
            sin_angle = np.sin(angle)
            a = np.sin((1-t)*angle) / sin_angle
            b = np.sin(t*angle) / sin_angle
            point = a * start_norm + b * end_norm
            great_circle_points.append(sphere_center + point)
        
        great_circle = CurvesAsSubmobjects(VMobject().set_points_smoothly(great_circle_points))
        great_circle.set_color(YELLOW)
        
        # Position the label with proper spacing
        curved_label = Text("Curved Space", font_size=24)
        curved_label.next_to(sphere, UP, buff=0.5)
        
        self.play(
            Create(flat_plane), 
            FadeIn(point_a), 
            FadeIn(point_b),
            Create(sphere),
            FadeIn(sphere_point_a),
            FadeIn(sphere_point_b), 
            run_time=2
        )
        
        self.play(
            Write(flat_label),
            Write(curved_label),
            run_time=1
        )
        
        self.play(
            Create(flat_line),
            Create(great_circle),
            run_time=3
        )
        
        # Add geodesic equation with proper spacing
        geodesic_eq = MathTex(r"\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0")
        geodesic_eq.scale(0.6).to_edge(DOWN, buff=0.8)
        
        self.play(Write(geodesic_eq), run_time=1)
        self.wait(1)
        
        # [0:52-1:05] Return to spacetime grid with multiple masses
        self.play(
            FadeOut(flat_plane),
            FadeOut(point_a),
            FadeOut(point_b),
            FadeOut(flat_line),
            FadeOut(flat_label),
            FadeOut(sphere),
            FadeOut(sphere_point_a),
            FadeOut(sphere_point_b),
            FadeOut(great_circle),
            FadeOut(curved_label),
            FadeOut(geodesic_eq),
            run_time=2
        )
        
        # Create new spacetime grid with padding
        grid = NumberPlane(
            x_range=(-8, 8, 1),
            y_range=(-4.5, 4.5, 1),
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        # Scale grid to leave space around edges
        grid.scale(0.9)
        
        # Create multiple masses with different sizes and proper spacing
        mass1 = Sphere(radius=0.7, resolution=(20, 20)).set_color(YELLOW).move_to(np.array([-3, 1, 0]))
        mass2 = Sphere(radius=0.4, resolution=(20, 20)).set_color(RED).move_to(np.array([2, -2, 0]))
        mass3 = Sphere(radius=1.0, resolution=(20, 20)).set_color(BLUE_E).move_to(np.array([3, 2, 0]))
        
        # Create curved grid with multiple centers
        curved_grid_multi = grid.copy()
        centers = [mass1.get_center(), mass2.get_center(), mass3.get_center()]
        intensities = [0.25, 0.12, 0.4]  # Proportional to masses
        
        for mob in curved_grid_multi.family_members_with_points():
            points = mob.get_points()
            for i, point in enumerate(points):
                # Apply cumulative effect from all masses
                z_offset = 0
                for center, intensity in zip(centers, intensities):
                    dist = np.linalg.norm(point[:2] - center[:2])
                    if dist < 4:
                        z_offset += -intensity * max(0, (4 - dist)**2)
                points[i][2] = z_offset
        
        self.play(Create(grid), run_time=1)
        self.play(
            Transform(grid, curved_grid_multi),
            FadeIn(mass1),
            FadeIn(mass2),
            FadeIn(mass3),
            run_time=3
        )
        
        # Create light rays being bent around masses
        def create_light_ray(start_point, end_point, num_points=40):
            # Create a curved path for the light ray
            points = []
            start = np.array([float(start_point[0]), float(start_point[1]), 0.0])
            end = np.array([float(end_point[0]), float(end_point[1]), 0.0])
            
            for t in np.linspace(0, 1, num_points):
                # Straight line interpolation
                base_point = start * (1-t) + end * t
                
                # Apply curvature based on proximity to masses
                z_offset = 0.0
                for center, intensity in zip(centers, intensities):
                    dist = np.linalg.norm(base_point[:2] - center[:2])
                    if dist < 4:
                        z_offset += -intensity * max(0, (4 - dist)**2)
                
                # Initialize deflection as float array to prevent type issues
                deflection = np.array([0.0, 0.0, 0.0])
                for center, intensity in zip(centers, intensities):
                    dist = np.linalg.norm(base_point[:2] - center[:2])
                    if dist < 4 and dist > 0.5:
                        direction = base_point[:2] - center[:2]
                        deflection_strength = intensity * (4 - dist) / (dist**2) * 0.3
                        deflection += np.array([
                            -direction[1] * deflection_strength,
                            direction[0] * deflection_strength,
                            0.0  # Use float
                        ])
                
                curved_point = base_point + deflection
                curved_point[2] = z_offset
                points.append(curved_point)
            
            return CurvesAsSubmobjects(VMobject().set_points_smoothly(points))
        
        # Create light rays with proper spacing
        light_ray1 = create_light_ray([-7, 3], [7, -3])
        light_ray2 = create_light_ray([-7, -1], [7, 3])
        light_ray3 = create_light_ray([-7, -3], [7, 1])
        
        # Style light rays
        for ray in [light_ray1, light_ray2, light_ray3]:
            ray.set_color(YELLOW)
            ray.set_stroke(width=3, opacity=0.8)
        
        # Animate light rays appearing sequentially with proper timing
        self.play(Create(light_ray1), run_time=1.5)
        self.play(Create(light_ray2), run_time=1.5)
        self.play(Create(light_ray3), run_time=1.5)
        
        # Add final Einstein field equation with proper spacing
        einstein_eq = MathTex(
            r"G_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}",
            font_size=42
        )
        einstein_eq.to_edge(UP, buff=1)
        
        self.play(
            Write(einstein_eq),
            run_time=2
        )
        
        # Create a 3Blue1Brown ending logo with proper spacing
        logo_circle = Circle(radius=0.5, color=BLUE)
        logo_circle.set_fill(BLUE, opacity=1)
        logo_triangle = Triangle(color=WHITE)
        logo_triangle.set_fill(WHITE, opacity=1)
        logo_triangle.scale(0.3)
        logo_triangle.rotate(PI/2)  # Point upward
        logo_triangle.shift(UP * 0.1)  # Center in the circle
        
        logo = VGroup(logo_circle, logo_triangle)
        logo.scale(0.7)
        logo.to_edge(DOWN, buff=0.8)
        
        self.play(
            FadeOut(einstein_eq, shift=UP),
            FadeIn(logo, scale=1.2),
            run_time=2
        )
        
        self.wait(1)