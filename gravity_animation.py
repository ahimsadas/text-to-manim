from manim import *
import numpy as np

# 3Blue1Brown style colors
BLUE_E = "#1C758A"
BACKGROUND_COLOR = "#000000"
BLUE_COLOR = "#58C4DD"
YELLOW_COLOR = "#FFFF00"
GREEN_COLOR = "#83C167"

class GravityAnimation(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Scene 1: Objects falling in vacuum
        self.scene_one()
        
        # Scene 2: Gravity equation and Earth
        self.scene_two()
        
        # Scene 3: Falling objects with velocity vectors
        self.scene_three()
        
        # Scene 4: Velocity-time graph
        self.scene_four()
        
        # Scene 5: Mass independence
        self.scene_five()
        
        # Scene 6: Spacetime curvature
        self.scene_six()

    def scene_one(self):
        # Initial text
        title = Text("Imagine dropping two objects from the same height.", font_size=40)
        title.to_edge(UP)
        
        # Create feather and bowling ball
        feather = SVGMobject("feather.svg").scale(0.5)
        bowling_ball = Circle(radius=0.5, color=GREY, fill_opacity=1)
        
        feather.move_to(LEFT * 3 + UP * 2)
        bowling_ball.move_to(RIGHT * 3 + UP * 2)
        
        # Create ground
        ground = Line(LEFT * 7, RIGHT * 7, color=YELLOW_COLOR)
        ground.move_to(DOWN * 2)
        
        # Vacuum chamber
        chamber = Rectangle(height=5, width=8, color=BLUE_COLOR).set_opacity(0.2)
        chamber.move_to(DOWN * 0.5)
        chamber_label = Text("Vacuum Chamber", font_size=30, color=BLUE_COLOR)
        chamber_label.next_to(chamber, UP)
        
        # Show initial setup
        self.play(Write(title), run_time=2)
        self.play(
            FadeIn(feather), 
            FadeIn(bowling_ball),
            Create(ground),
            run_time=1.5
        )
        self.wait()
        
        # Show vacuum chamber
        self.play(
            FadeIn(chamber),
            Write(chamber_label),
            run_time=1.5
        )
        self.wait()
        
        # Objects falling animation
        self.play(
            feather.animate.move_to(LEFT * 3 + DOWN * 2),
            bowling_ball.animate.move_to(RIGHT * 3 + DOWN * 2),
            rate_func=rate_functions.linear,
            run_time=2
        )
        
        # Impact flash
        flash1 = Dot(color=WHITE, radius=0.1).move_to(LEFT * 3 + DOWN * 2)
        flash2 = Dot(color=WHITE, radius=0.1).move_to(RIGHT * 3 + DOWN * 2)
        
        self.play(
            flash1.animate.scale(5).set_opacity(0),
            flash2.animate.scale(5).set_opacity(0),
            run_time=0.5
        )
        
        # Second text
        conclusion_text = Text("In a vacuum, they hit the ground simultaneously. Why?", font_size=40)
        conclusion_text.to_edge(UP)
        
        self.play(
            FadeOut(title),
            Write(conclusion_text),
            run_time=1.5
        )
        self.wait(2)
        
        # Clean up scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

    def scene_two(self):
        # Display g equation
        equation = MathTex(r"g = 9.8 \frac{m}{s^2}", font_size=80)
        equation.set_color(BLUE_COLOR)
        
        self.play(Write(equation), run_time=1.5)
        self.wait()
        
        # Move equation up
        self.play(equation.animate.to_edge(UP), run_time=1)
        
        # Text explanation
        explanation = Text(
            "This is acceleration due to gravity - a constant force\npulling objects toward Earth's center.",
            font_size=36, line_spacing=0.5
        )
        explanation.next_to(equation, DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=2)
        self.wait()
        
        # Create Earth
        earth = Circle(radius=2, color=BLUE_E)
        earth.set_fill(BLUE_E, opacity=1)
        
        # Add continents
        continents = VMobject()
        # Very simplified continent shapes
        continents.set_points_as_corners([
            UP * 0.8 + LEFT * 0.5,
            UP * 0.4 + RIGHT * 0.8,
            DOWN * 0.3 + RIGHT * 1.1,
            DOWN * 0.7 + LEFT * 0.2,
            UP * 0.2 + LEFT * 0.9,
            UP * 0.8 + LEFT * 0.5
        ])
        continents.set_fill(GREEN_COLOR, opacity=1)
        continents.set_stroke(width=0)
        
        earth_group = VGroup(earth, continents)
        earth_group.scale(0.8)
        earth_group.move_to(DOWN * 0.5)
        
        # Fade out equation and text, fade in Earth
        self.play(
            FadeOut(equation),
            FadeOut(explanation),
            FadeIn(earth_group),
            run_time=1.5
        )
        
        # Create objects around Earth
        objects = VGroup()
        positions = [
            UP * 2.5,
            RIGHT * 2.5,
            DOWN * 2.5,
            LEFT * 2.5,
            UP * 1.8 + RIGHT * 1.8,
            DOWN * 1.8 + RIGHT * 1.8,
            DOWN * 1.8 + LEFT * 1.8,
            UP * 1.8 + LEFT * 1.8
        ]
        
        for pos in positions:
            obj = Square(side_length=0.2, color=YELLOW_COLOR, fill_opacity=1)
            obj.move_to(pos)
            objects.add(obj)
        
        # Show objects
        self.play(FadeIn(objects), run_time=1)
        
        # Add arrows pointing toward Earth's center
        arrows = VGroup()
        for obj in objects:
            direction = earth.get_center() - obj.get_center()
            direction = direction / np.linalg.norm(direction)
            arrow = Arrow(
                start=obj.get_center(),
                end=obj.get_center() + direction * 0.8,
                color=YELLOW_COLOR,
                buff=0.1
            )
            arrows.add(arrow)
        
        self.play(Create(arrows), run_time=1.5)
        self.wait(2)
        
        # Clean up scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

    def scene_three(self):
        # Set up ground and objects
        ground = Line(LEFT * 7, RIGHT * 7, color=YELLOW_COLOR)
        ground.move_to(DOWN * 3)
        
        ball1 = Circle(radius=0.3, color=BLUE_COLOR, fill_opacity=1)
        ball2 = Circle(radius=0.3, color=RED, fill_opacity=1)
        
        ball1.move_to(LEFT * 2 + UP * 2)
        ball2.move_to(RIGHT * 2 + UP * 2)
        
        # Create velocity vectors
        v1_initial = Arrow(
            start=ball1.get_center(),
            end=ball1.get_center() + DOWN * 0.5,
            color=YELLOW_COLOR,
            buff=0.1
        )
        v2_initial = Arrow(
            start=ball2.get_center(),
            end=ball2.get_center() + DOWN * 0.5,
            color=YELLOW_COLOR,
            buff=0.1
        )
        
        # Labels for vectors
        v1_label = MathTex(r"9.8 \frac{m}{s}", font_size=30, color=YELLOW_COLOR)
        v1_label.next_to(v1_initial, RIGHT, buff=0.1)
        v2_label = MathTex(r"9.8 \frac{m}{s}", font_size=30, color=YELLOW_COLOR)
        v2_label.next_to(v2_initial, LEFT, buff=0.1)
        
        # Title
        title = Text("Each second, an object's velocity increases by 9.8 m/s.", font_size=36)
        title.to_edge(UP)
        
        # Show initial setup
        self.play(
            Create(ground),
            FadeIn(ball1),
            FadeIn(ball2),
            Write(title),
            run_time=1.5
        )
        self.wait()
        
        # Show initial velocity vectors
        self.play(
            GrowArrow(v1_initial),
            GrowArrow(v2_initial),
            Write(v1_label),
            Write(v2_label),
            run_time=1
        )
        self.wait()
        
        # Define positions and velocities for animation
        positions = []
        velocities = []
        times = [0, 0.5, 1, 1.5]
        
        for t in times:
            # s = 0.5 * g * t^2 formula for position
            pos = 2 - 0.5 * 9.8 * t * t  # Starting at y=2
            vel = 9.8 * t  # v = g * t
            positions.append(pos)
            velocities.append(vel)
        
        # Animate falling with changing vectors
        for i in range(1, len(times)):
            # Update ball positions
            new_pos1 = LEFT * 2 + UP * positions[i]
            new_pos2 = RIGHT * 2 + UP * positions[i]
            
            # Create new velocity vectors
            v1_new = Arrow(
                start=new_pos1,
                end=new_pos1 + DOWN * (velocities[i] / 9.8),  # Scale for visibility
                color=YELLOW_COLOR,
                buff=0.1
            )
            v2_new = Arrow(
                start=new_pos2,
                end=new_pos2 + DOWN * (velocities[i] / 9.8),
                color=YELLOW_COLOR,
                buff=0.1
            )
            
            # Update labels
            v1_new_label = MathTex(f"{velocities[i]:.1f} \\frac{{m}}{{s}}", font_size=30, color=YELLOW_COLOR)
            v1_new_label.next_to(v1_new, RIGHT, buff=0.1)
            v2_new_label = MathTex(f"{velocities[i]:.1f} \\frac{{m}}{{s}}", font_size=30, color=YELLOW_COLOR)
            v2_new_label.next_to(v2_new, LEFT, buff=0.1)
            
            # Animate the transition
            self.play(
                ball1.animate.move_to(new_pos1),
                ball2.animate.move_to(new_pos2),
                Transform(v1_initial, v1_new),
                Transform(v2_initial, v2_new),
                Transform(v1_label, v1_new_label),
                Transform(v2_label, v2_new_label),
                run_time=times[i] - times[i-1]
            )
        
        self.wait(2)
        
        # Clean up scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )

    def scene_four(self):
        # Create axes for velocity-time graph
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 50, 10],
            axis_config={"color": WHITE},
            x_length=9,
            y_length=5,
            tips=True
        )
        
        # Add labels
        x_label = Text("Time (s)", font_size=24)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("Velocity (m/s)", font_size=24)
        y_label.next_to(axes.y_axis, LEFT)
        origin_label = Text("0", font_size=20)
        origin_label.next_to(axes.c2p(0, 0), DOWN+LEFT, buff=0.1)
        
        graph_title = Text("Velocity vs. Time for Falling Object", font_size=36)
        graph_title.to_edge(UP)
        
        # Create the velocity-time graph
        graph = axes.plot(
            lambda x: 9.8 * x,
            x_range=[0, 5],
            color=BLUE_COLOR
        )
        
        # Dot for tracking position on graph
        dot = Dot(color=YELLOW_COLOR)
        dot.move_to(axes.c2p(0, 0))
        
        # Create velocity graph group
        graph_group = VGroup(axes, x_label, y_label, origin_label, graph_title)
        
        # Show the graph
        self.play(
            Write(graph_title),
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(origin_label),
            run_time=2
        )
        self.wait()
        
        # Animate drawing the graph with the dot
        self.add(dot)
        self.play(
            Create(graph),
            MoveAlongPath(dot, graph),
            run_time=3
        )
        self.wait()
        
        # Highlight constant slope
        slope_line1 = Line(
            axes.c2p(1, 9.8),
            axes.c2p(1, 0),
            color=YELLOW_COLOR
        )
        slope_line2 = Line(
            axes.c2p(2, 19.6),
            axes.c2p(2, 0),
            color=YELLOW_COLOR
        )
        
        slope_arrow = Arrow(
            axes.c2p(1, 4.9),
            axes.c2p(2, 4.9),
            color=YELLOW_COLOR,
            buff=0.1
        )
        
        slope_text = MathTex(r"9.8 \frac{m}{s^2}", font_size=36, color=YELLOW_COLOR)
        slope_text.next_to(slope_arrow, UP, buff=0.2)
        
        self.play(
            Create(slope_line1),
            Create(slope_line2),
            run_time=1
        )
        self.play(
            GrowArrow(slope_arrow),
            Write(slope_text),
            run_time=1.5
        )
        self.wait()
        
        # Add text about constant slope
        explanation = Text("This constant slope represents acceleration.", font_size=36)
        explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(2)
        
        # Clean up scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
    
    def scene_five(self):
        # Create objects with different masses
        title = Text("What's remarkable is this acceleration is independent of mass.", font_size=36)
        title.to_edge(UP)
        
        # Create a small ball and a large ball
        small_ball = Circle(radius=0.3, color=BLUE_COLOR, fill_opacity=1)
        large_ball = Circle(radius=0.6, color=RED, fill_opacity=1)
        
        small_ball_label = Text("Small mass", font_size=24)
        small_ball_label.next_to(small_ball, UP, buff=0.3)
        large_ball_label = Text("Large mass", font_size=24)
        large_ball_label.next_to(large_ball, UP, buff=0.3)
        
        small_ball.move_to(LEFT * 3 + UP * 1)
        large_ball.move_to(RIGHT * 3 + UP * 1)
        
        # Create ground
        ground = Line(LEFT * 7, RIGHT * 7, color=YELLOW_COLOR)
        ground.move_to(DOWN * 2.5)
        
        # Show initial setup
        self.play(
            Write(title),
            run_time=2
        )
        self.play(
            FadeIn(small_ball),
            FadeIn(large_ball),
            Write(small_ball_label),
            Write(large_ball_label),
            Create(ground),
            run_time=1.5
        )
        self.wait()
        
        # Add identical acceleration vectors
        acc_vector1 = Arrow(
            start=small_ball.get_center(),
            end=small_ball.get_center() + DOWN * 1,
            color=YELLOW_COLOR,
            buff=0.1
        )
        acc_vector2 = Arrow(
            start=large_ball.get_center(),
            end=large_ball.get_center() + DOWN * 1,
            color=YELLOW_COLOR,
            buff=0.1
        )
        
        acc_label1 = MathTex(r"g = 9.8 \frac{m}{s^2}", font_size=24, color=YELLOW_COLOR)
        acc_label1.next_to(acc_vector1, RIGHT, buff=0.1)
        acc_label2 = MathTex(r"g = 9.8 \frac{m}{s^2}", font_size=24, color=YELLOW_COLOR)
        acc_label2.next_to(acc_vector2, LEFT, buff=0.1)
        
        self.play(
            GrowArrow(acc_vector1),
            GrowArrow(acc_vector2),
            Write(acc_label1),
            Write(acc_label2),
            run_time=1.5
        )
        self.wait()
        
        # Animate falling with identical acceleration
        self.play(
            small_ball.animate.move_to(LEFT * 3 + DOWN * 2.5),
            large_ball.animate.move_to(RIGHT * 3 + DOWN * 2.5),
            acc_vector1.animate.shift(DOWN * 3.5),
            acc_vector2.animate.shift(DOWN * 3.5),
            acc_label1.animate.shift(DOWN * 3.5),
            acc_label2.animate.shift(DOWN * 3.5),
            small_ball_label.animate.shift(DOWN * 3.5),
            large_ball_label.animate.shift(DOWN * 3.5),
            rate_func=rate_functions.smooth,
            run_time=2
        )
        
        # Impact flashes
        flash1 = Dot(color=WHITE, radius=0.1).move_to(LEFT * 3 + DOWN * 2.5)
        flash2 = Dot(color=WHITE, radius=0.1).move_to(RIGHT * 3 + DOWN * 2.5)
        
        self.play(
            flash1.animate.scale(5).set_opacity(0),
            flash2.animate.scale(5).set_opacity(0),
            run_time=0.5
        )
        self.wait(2)
        
        # Clean up scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1
        )
    
    def scene_six(self):
        # Create final scene with spacetime curvature
        title = Text("Einstein's insight was recognizing that gravity isn't just a force,", font_size=36)
        subtitle = Text("but the curvature of spacetime itself.", font_size=36)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        
        self.play(
            Write(title),
            run_time=2
        )
        self.play(
            Write(subtitle),
            run_time=2
        )
        self.wait()
        
        # Move titles up to make room for visualization
        self.play(
            title.animate.shift(UP * 0.5),
            subtitle.animate.shift(UP * 0.5),
            run_time=1
        )
        
        # Create a 3D grid for spacetime
        # Since manim doesn't easily support full 3D, we'll create a 2D grid with perspective
        
        # Base grid (flat)
        rows, cols = 15, 15
        grid = VGroup()
        grid_spacing = 0.3
        
        # Create horizontal and vertical lines
        for i in range(rows + 1):
            y = i * grid_spacing - rows * grid_spacing / 2
            h_line = Line(LEFT * cols * grid_spacing / 2, RIGHT * cols * grid_spacing / 2, color=BLUE_E, stroke_width=1)
            h_line.move_to([0, y, 0])
            grid.add(h_line)
        
        for j in range(cols + 1):
            x = j * grid_spacing - cols * grid_spacing / 2
            v_line = Line(UP * rows * grid_spacing / 2, DOWN * rows * grid_spacing / 2, color=BLUE_E, stroke_width=1)
            v_line.move_to([x, 0, 0])
            grid.add(v_line)
        
        # Position grid
        grid.move_to(DOWN * 0.5)
        grid.scale(1.2)
        
        # Show initial grid
        self.play(Create(grid), run_time=2)
        
        # Create Earth (sphere in the center)
        earth = Circle(radius=1.2, color=BLUE_COLOR)
        earth.set_fill(BLUE_COLOR, opacity=0.8)
        earth.move_to(grid.get_center())
        
        # Deform grid to show spacetime curvature
        # We'll use a radial deformation function
        def deform_point(point, center, strength=0.5):
            # Distance from center
            diff = point - center
            dist = np.linalg.norm(diff)
            if dist < 0.1:  # Avoid division by very small numbers
                return point
            
            # Calculate displacement (more displacement closer to center)
            displacement = strength / (dist ** 0.7)  # Adjust the exponent for different curvature profiles
            return point - diff * displacement
        
        # Apply deformation to grid points
        deformed_grid = grid.copy()
        center = earth.get_center()
        
        for line in deformed_grid:
            points = line.get_points()
            new_points = np.array([deform_point(p, center) for p in points])
            line.set_points(new_points)
        
        # Animate the deformation
        self.play(
            Transform(grid, deformed_grid),
            FadeIn(earth),
            run_time=2.5
        )
        self.wait()
        
        # Add falling objects following curved spacetime
        obj1 = Dot(color=YELLOW_COLOR)
        obj1.move_to(earth.get_center() + UP * 3.5 + LEFT * 1)
        
        obj2 = Dot(color=RED)
        obj2.move_to(earth.get_center() + UP * 3.5 + RIGHT * 1)
        
        self.play(FadeIn(obj1), FadeIn(obj2), run_time=1)
        
        # Create curved paths for the objects
        def curved_path_to_center(start_point, center, steps=50):
            path = VMobject()
            points = []
            
            for i in range(steps + 1):
                t = i / steps
                # Linear interpolation + curve toward center
                intermediate = start_point * (1 - t) + center * t
                # Add additional curve
                if 0.1 < t < 0.9:
                    # Adjust the curve based on distance to center
                    vec_to_center = center - start_point
                    perp_vec = np.array([-vec_to_center[1], vec_to_center[0], 0])
                    perp_vec = perp_vec / np.linalg.norm(perp_vec)
                    curve_factor = 0.5 * np.sin(t * np.pi)
                    intermediate += perp_vec * curve_factor
                
                points.append(intermediate)
            
            path.set_points_as_corners(points)
            return path
        
        path1 = curved_path_to_center(obj1.get_center(), earth.get_center())
        path2 = curved_path_to_center(obj2.get_center(), earth.get_center())
        
        # Animate objects following curved paths
        self.play(
            MoveAlongPath(obj1, path1),
            MoveAlongPath(obj2, path2),
            run_time=3
        )
        
        # Final message
        final_message = Text("Objects follow the curved geometry of spacetime", font_size=32)
        final_message.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_message), run_time=1.5)
        self.wait(3)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

class SceneOne(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Initial text
        title = Text("Imagine dropping two objects from the same height.", font_size=40)
        title.to_edge(UP)
        
        # Create feather and bowling ball
        feather = SVGMobject("feather.svg").scale(0.5)
        bowling_ball = Circle(radius=0.5, color=GREY, fill_opacity=1)
        
        feather.move_to(LEFT * 3 + UP * 2)
        bowling_ball.move_to(RIGHT * 3 + UP * 2)
        
        # Create ground
        ground = Line(LEFT * 7, RIGHT * 7, color=YELLOW_COLOR)
        ground.move_to(DOWN * 2)
        
        # Vacuum chamber
        chamber = Rectangle(height=5, width=8, color=BLUE_COLOR).set_opacity(0.2)
        chamber.move_to(DOWN * 0.5)
        chamber_label = Text("Vacuum Chamber", font_size=30, color=BLUE_COLOR)
        chamber_label.next_to(chamber, UP)
        
        # Show initial setup
        self.play(Write(title), run_time=2)
        self.play(
            FadeIn(feather), 
            FadeIn(bowling_ball),
            Create(ground),
            run_time=1.5
        )
        self.wait()
        
        # Show vacuum chamber
        self.play(
            FadeIn(chamber),
            Write(chamber_label),
            run_time=1.5
        )
        self.wait()
        
        # Objects falling animation
        self.play(
            feather.animate.move_to(LEFT * 3 + DOWN * 2),
            bowling_ball.animate.move_to(RIGHT * 3 + DOWN * 2),
            rate_func=rate_functions.linear,
            run_time=2
        )
        
        # Impact flash
        flash1 = Dot(color=WHITE, radius=0.1).move_to(LEFT * 3 + DOWN * 2)
        flash2 = Dot(color=WHITE, radius=0.1).move_to(RIGHT * 3 + DOWN * 2)
        
        self.play(
            flash1.animate.scale(5).set_opacity(0),
            flash2.animate.scale(5).set_opacity(0),
            run_time=0.5
        )
        
        # Second text
        conclusion_text = Text("In a vacuum, they hit the ground simultaneously. Why?", font_size=40)
        conclusion_text.to_edge(UP)
        
        self.play(
            FadeOut(title),
            Write(conclusion_text),
            run_time=1.5
        )
        self.wait(2)

# Add individual scene classes for the remaining scenes
class SceneTwo(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Display g equation
        equation = MathTex(r"g = 9.8 \frac{m}{s^2}", font_size=80)
        equation.set_color(BLUE_COLOR)
        
        self.play(Write(equation), run_time=1.5)
        self.wait()
        
        # Move equation up
        self.play(equation.animate.to_edge(UP), run_time=1)
        
        # Text explanation
        explanation = Text(
            "This is acceleration due to gravity - a constant force\npulling objects toward Earth's center.",
            font_size=36, line_spacing=0.5
        )
        explanation.next_to(equation, DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=2)
        self.wait()
        
        # Create Earth
        earth = Circle(radius=2, color=BLUE_E)
        earth.set_fill(BLUE_E, opacity=1)
        
        # Add continents
        continents = VMobject()
        # Very simplified continent shapes
        continents.set_points_as_corners([
            UP * 0.8 + LEFT * 0.5,
            UP * 0.4 + RIGHT * 0.8,
            DOWN * 0.3 + RIGHT * 1.1,
            DOWN * 0.7 + LEFT * 0.2,
            UP * 0.2 + LEFT * 0.9,
            UP * 0.8 + LEFT * 0.5
        ])
        continents.set_fill(GREEN_COLOR, opacity=1)
        continents.set_stroke(width=0)
        
        earth_group = VGroup(earth, continents)
        earth_group.scale(0.8)
        earth_group.move_to(DOWN * 0.5)
        
        # Fade out equation and text, fade in Earth
        self.play(
            FadeOut(equation),
            FadeOut(explanation),
            FadeIn(earth_group),
            run_time=1.5
        )
        
        # Create objects around Earth
        objects = VGroup()
        positions = [
            UP * 2.5,
            RIGHT * 2.5,
            DOWN * 2.5,
            LEFT * 2.5,
            UP * 1.8 + RIGHT * 1.8,
            DOWN * 1.8 + RIGHT * 1.8,
            DOWN * 1.8 + LEFT * 1.8,
            UP * 1.8 + LEFT * 1.8
        ]
        
        for pos in positions:
            obj = Square(side_length=0.2, color=YELLOW_COLOR, fill_opacity=1)
            obj.move_to(pos)
            objects.add(obj)
        
        # Show objects
        self.play(FadeIn(objects), run_time=1)
        
        # Add arrows pointing toward Earth's center
        arrows = VGroup()
        for obj in objects:
            direction = earth.get_center() - obj.get_center()
            direction = direction / np.linalg.norm(direction)
            arrow = Arrow(
                start=obj.get_center(),
                end=obj.get_center() + direction * 0.8,
                color=YELLOW_COLOR,
                buff=0.1
            )
            arrows.add(arrow)
        
        self.play(Create(arrows), run_time=1.5)
        self.wait(2)

class SceneThree(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Set up ground and objects
        ground = Line(LEFT * 7, RIGHT * 7, color=YELLOW_COLOR)
        ground.move_to(DOWN * 3)
        
        ball1 = Circle(radius=0.3, color=BLUE_COLOR, fill_opacity=1)
        ball2 = Circle(radius=0.3, color=RED, fill_opacity=1)
        
        ball1.move_to(LEFT * 2 + UP * 2)
        ball2.move_to(RIGHT * 2 + UP * 2)
        
        # Create velocity vectors
        v1_initial = Arrow(
            start=ball1.get_center(),
            end=ball1.get_center() + DOWN * 0.5,
            color=YELLOW_COLOR,
            buff=0.1
        )
        v2_initial = Arrow(
            start=ball2.get_center(),
            end=ball2.get_center() + DOWN * 0.5,
            color=YELLOW_COLOR,
            buff=0.1
        )
        
        # Labels for vectors
        v1_label = MathTex(r"9.8 \frac{m}{s}", font_size=30, color=YELLOW_COLOR)
        v1_label.next_to(v1_initial, RIGHT, buff=0.1)
        v2_label = MathTex(r"9.8 \frac{m}{s}", font_size=30, color=YELLOW_COLOR)
        v2_label.next_to(v2_initial, LEFT, buff=0.1)
        
        # Title
        title = Text("Each second, an object's velocity increases by 9.8 m/s.", font_size=36)
        title.to_edge(UP)
        
        # Show initial setup
        self.play(
            Create(ground),
            FadeIn(ball1),
            FadeIn(ball2),
            Write(title),
            run_time=1.5
        )
        self.wait()
        
        # Show initial velocity vectors
        self.play(
            GrowArrow(v1_initial),
            GrowArrow(v2_initial),
            Write(v1_label),
            Write(v2_label),
            run_time=1
        )
        self.wait()
        
        # Define positions and velocities for animation
        positions = []
        velocities = []
        times = [0, 0.5, 1, 1.5]
        
        for t in times:
            # s = 0.5 * g * t^2 formula for position
            pos = 2 - 0.5 * 9.8 * t * t  # Starting at y=2
            vel = 9.8 * t  # v = g * t
            positions.append(pos)
            velocities.append(vel)
        
        # Animate falling with changing vectors
        for i in range(1, len(times)):
            # Update ball positions
            new_pos1 = LEFT * 2 + UP * positions[i]
            new_pos2 = RIGHT * 2 + UP * positions[i]
            
            # Create new velocity vectors
            v1_new = Arrow(
                start=new_pos1,
                end=new_pos1 + DOWN * (velocities[i] / 9.8),  # Scale for visibility
                color=YELLOW_COLOR,
                buff=0.1
            )
            v2_new = Arrow(
                start=new_pos2,
                end=new_pos2 + DOWN * (velocities[i] / 9.8),
                color=YELLOW_COLOR,
                buff=0.1
            )
            
            # Update labels
            v1_new_label = MathTex(f"{velocities[i]:.1f} \\frac{{m}}{{s}}", font_size=30, color=YELLOW_COLOR)
            v1_new_label.next_to(v1_new, RIGHT, buff=0.1)
            v2_new_label = MathTex(f"{velocities[i]:.1f} \\frac{{m}}{{s}}", font_size=30, color=YELLOW_COLOR)
            v2_new_label.next_to(v2_new, LEFT, buff=0.1)
            
            # Animate the transition
            self.play(
                ball1.animate.move_to(new_pos1),
                ball2.animate.move_to(new_pos2),
                Transform(v1_initial, v1_new),
                Transform(v2_initial, v2_new),
                Transform(v1_label, v1_new_label),
                Transform(v2_label, v2_new_label),
                run_time=times[i] - times[i-1]
            )
        
        self.wait(2)

class SceneFour(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create axes for velocity-time graph
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 50, 10],
            axis_config={"color": WHITE},
            x_length=9,
            y_length=5,
            tips=True
        )
        
        # Add labels
        x_label = Text("Time (s)", font_size=24)
        x_label.next_to(axes.x_axis, DOWN)
        y_label = Text("Velocity (m/s)", font_size=24)
        y_label.next_to(axes.y_axis, LEFT)
        origin_label = Text("0", font_size=20)
        origin_label.next_to(axes.c2p(0, 0), DOWN+LEFT, buff=0.1)
        
        graph_title = Text("Velocity vs. Time for Falling Object", font_size=36)
        graph_title.to_edge(UP)
        
        # Create the velocity-time graph
        graph = axes.plot(
            lambda x: 9.8 * x,
            x_range=[0, 5],
            color=BLUE_COLOR
        )
        
        # Dot for tracking position on graph
        dot = Dot(color=YELLOW_COLOR)
        dot.move_to(axes.c2p(0, 0))
        
        # Create velocity graph group
        graph_group = VGroup(axes, x_label, y_label, origin_label, graph_title)
        
        # Show the graph
        self.play(
            Write(graph_title),
            Create(axes),
            Write(x_label),
            Write(y_label),
            Write(origin_label),
            run_time=2
        )
        self.wait()
        
        # Animate drawing the graph with the dot
        self.add(dot)
        self.play(
            Create(graph),
            MoveAlongPath(dot, graph),
            run_time=3
        )
        self.wait()
        
        # Highlight constant slope
        slope_line1 = Line(
            axes.c2p(1, 9.8),
            axes.c2p(1, 0),
            color=YELLOW_COLOR
        )
        slope_line2 = Line(
            axes.c2p(2, 19.6),
            axes.c2p(2, 0),
            color=YELLOW_COLOR
        )
        
        slope_arrow = Arrow(
            axes.c2p(1, 4.9),
            axes.c2p(2, 4.9),
            color=YELLOW_COLOR,
            buff=0.1
        )
        
        slope_text = MathTex(r"9.8 \frac{m}{s^2}", font_size=36, color=YELLOW_COLOR)
        slope_text.next_to(slope_arrow, UP, buff=0.2)
        
        self.play(
            Create(slope_line1),
            Create(slope_line2),
            run_time=1
        )
        self.play(
            GrowArrow(slope_arrow),
            Write(slope_text),
            run_time=1.5
        )
        self.wait()
        
        # Add text about constant slope
        explanation = Text("This constant slope represents acceleration.", font_size=36)
        explanation.to_edge(DOWN, buff=0.5)
        
        self.play(Write(explanation), run_time=1.5)
        self.wait(2)

class SceneFive(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create objects with different masses
        title = Text("What's remarkable is this acceleration is independent of mass.", font_size=36)
        title.to_edge(UP)
        
        # Create a small ball and a large ball
        small_ball = Circle(radius=0.3, color=BLUE_COLOR, fill_opacity=1)
        large_ball = Circle(radius=0.6, color=RED, fill_opacity=1)
        
        small_ball_label = Text("Small mass", font_size=24)
        small_ball_label.next_to(small_ball, UP, buff=0.3)
        large_ball_label = Text("Large mass", font_size=24)
        large_ball_label.next_to(large_ball, UP, buff=0.3)
        
        small_ball.move_to(LEFT * 3 + UP * 1)
        large_ball.move_to(RIGHT * 3 + UP * 1)
        
        # Create ground
        ground = Line(LEFT * 7, RIGHT * 7, color=YELLOW_COLOR)
        ground.move_to(DOWN * 2.5)
        
        # Show initial setup
        self.play(
            Write(title),
            run_time=2
        )
        self.play(
            FadeIn(small_ball),
            FadeIn(large_ball),
            Write(small_ball_label),
            Write(large_ball_label),
            Create(ground),
            run_time=1.5
        )
        self.wait()
        
        # Add identical acceleration vectors
        acc_vector1 = Arrow(
            start=small_ball.get_center(),
            end=small_ball.get_center() + DOWN * 1,
            color=YELLOW_COLOR,
            buff=0.1
        )
        acc_vector2 = Arrow(
            start=large_ball.get_center(),
            end=large_ball.get_center() + DOWN * 1,
            color=YELLOW_COLOR,
            buff=0.1
        )
        
        acc_label1 = MathTex(r"g = 9.8 \frac{m}{s^2}", font_size=24, color=YELLOW_COLOR)
        acc_label1.next_to(acc_vector1, RIGHT, buff=0.1)
        acc_label2 = MathTex(r"g = 9.8 \frac{m}{s^2}", font_size=24, color=YELLOW_COLOR)
        acc_label2.next_to(acc_vector2, LEFT, buff=0.1)
        
        self.play(
            GrowArrow(acc_vector1),
            GrowArrow(acc_vector2),
            Write(acc_label1),
            Write(acc_label2),
            run_time=1.5
        )
        self.wait()
        
        # Animate falling with identical acceleration
        self.play(
            small_ball.animate.move_to(LEFT * 3 + DOWN * 2.5),
            large_ball.animate.move_to(RIGHT * 3 + DOWN * 2.5),
            acc_vector1.animate.shift(DOWN * 3.5),
            acc_vector2.animate.shift(DOWN * 3.5),
            acc_label1.animate.shift(DOWN * 3.5),
            acc_label2.animate.shift(DOWN * 3.5),
            small_ball_label.animate.shift(DOWN * 3.5),
            large_ball_label.animate.shift(DOWN * 3.5),
            rate_func=rate_functions.smooth,
            run_time=2
        )
        
        # Impact flashes
        flash1 = Dot(color=WHITE, radius=0.1).move_to(LEFT * 3 + DOWN * 2.5)
        flash2 = Dot(color=WHITE, radius=0.1).move_to(RIGHT * 3 + DOWN * 2.5)
        
        self.play(
            flash1.animate.scale(5).set_opacity(0),
            flash2.animate.scale(5).set_opacity(0),
            run_time=0.5
        )
        self.wait(2)

class SceneSix(Scene):
    def construct(self):
        # Configure scene
        self.camera.background_color = BACKGROUND_COLOR
        
        # Create final scene with spacetime curvature
        title = Text("Einstein's insight was recognizing that gravity isn't just a force,", font_size=36)
        subtitle = Text("but the curvature of spacetime itself.", font_size=36)
        
        title.to_edge(UP)
        subtitle.next_to(title, DOWN)
        
        self.play(
            Write(title),
            run_time=2
        )
        self.play(
            Write(subtitle),
            run_time=2
        )
        self.wait()
        
        # Move titles up to make room for visualization
        self.play(
            title.animate.shift(UP * 0.5),
            subtitle.animate.shift(UP * 0.5),
            run_time=1
        )
        
        # Create a 3D grid for spacetime
        # Since manim doesn't easily support full 3D, we'll create a 2D grid with perspective
        
        # Base grid (flat)
        rows, cols = 15, 15
        grid = VGroup()
        grid_spacing = 0.3
        
        # Create horizontal and vertical lines
        for i in range(rows + 1):
            y = i * grid_spacing - rows * grid_spacing / 2
            h_line = Line(LEFT * cols * grid_spacing / 2, RIGHT * cols * grid_spacing / 2, color=BLUE_E, stroke_width=1)
            h_line.move_to([0, y, 0])
            grid.add(h_line)
        
        for j in range(cols + 1):
            x = j * grid_spacing - cols * grid_spacing / 2
            v_line = Line(UP * rows * grid_spacing / 2, DOWN * rows * grid_spacing / 2, color=BLUE_E, stroke_width=1)
            v_line.move_to([x, 0, 0])
            grid.add(v_line)
        
        # Position grid
        grid.move_to(DOWN * 0.5)
        grid.scale(1.2)
        
        # Show initial grid
        self.play(Create(grid), run_time=2)
        
        # Create Earth (sphere in the center)
        earth = Circle(radius=1.2, color=BLUE_COLOR)
        earth.set_fill(BLUE_COLOR, opacity=0.8)
        earth.move_to(grid.get_center())
        
        # Deform grid to show spacetime curvature
        # We'll use a radial deformation function
        def deform_point(point, center, strength=0.5):
            # Distance from center
            diff = point - center
            dist = np.linalg.norm(diff)
            if dist < 0.1:  # Avoid division by very small numbers
                return point
            
            # Calculate displacement (more displacement closer to center)
            displacement = strength / (dist ** 0.7)  # Adjust the exponent for different curvature profiles
            return point - diff * displacement
        
        # Apply deformation to grid points
        deformed_grid = grid.copy()
        center = earth.get_center()
        
        for line in deformed_grid:
            points = line.get_points()
            new_points = np.array([deform_point(p, center) for p in points])
            line.set_points(new_points)
        
        # Animate the deformation
        self.play(
            Transform(grid, deformed_grid),
            FadeIn(earth),
            run_time=2.5
        )
        self.wait()
        
        # Add falling objects following curved spacetime
        obj1 = Dot(color=YELLOW_COLOR)
        obj1.move_to(earth.get_center() + UP * 3.5 + LEFT * 1)
        
        obj2 = Dot(color=RED)
        obj2.move_to(earth.get_center() + UP * 3.5 + RIGHT * 1)
        
        self.play(FadeIn(obj1), FadeIn(obj2), run_time=1)
        
        # Create curved paths for the objects
        def curved_path_to_center(start_point, center, steps=50):
            path = VMobject()
            points = []
            
            for i in range(steps + 1):
                t = i / steps
                # Linear interpolation + curve toward center
                intermediate = start_point * (1 - t) + center * t
                # Add additional curve
                if 0.1 < t < 0.9:
                    # Adjust the curve based on distance to center
                    vec_to_center = center - start_point
                    perp_vec = np.array([-vec_to_center[1], vec_to_center[0], 0])
                    perp_vec = perp_vec / np.linalg.norm(perp_vec)
                    curve_factor = 0.5 * np.sin(t * np.pi)
                    intermediate += perp_vec * curve_factor
                
                points.append(intermediate)
            
            path.set_points_as_corners(points)
            return path
        
        path1 = curved_path_to_center(obj1.get_center(), earth.get_center())
        path2 = curved_path_to_center(obj2.get_center(), earth.get_center())
        
        # Animate objects following curved paths
        self.play(
            MoveAlongPath(obj1, path1),
            MoveAlongPath(obj2, path2),
            run_time=3
        )
        
        # Final message
        final_message = Text("Objects follow the curved geometry of spacetime", font_size=32)
        final_message.to_edge(DOWN, buff=0.5)
        
        self.play(Write(final_message), run_time=1.5)
        self.wait(3)
        
        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

# Main rendering order for creating the full video
if __name__ == "__main__":
    # Uncomment one of these to render:
    # For the complete animation:
    os.system("manim -pqh gravity_animation.py GravityAnimation")
    
    # For individual scenes:
    # os.system("manim -pqh gravity_animation.py SceneOne")
    # os.system("manim -pqh gravity_animation.py SceneTwo")
    # os.system("manim -pqh gravity_animation.py SceneThree")
    # os.system("manim -pqh gravity_animation.py SceneFour")
    # os.system("manim -pqh gravity_animation.py SceneFive")
    # os.system("manim -pqh gravity_animation.py SceneSix")

# You'll need to create/download a feather SVG file or replace it with a simple shape
# If you don't have a feather.svg, you can replace that line with:
# feather = Triangle().scale(0.5).set_fill(WHITE, opacity=1)