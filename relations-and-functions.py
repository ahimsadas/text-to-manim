from manim import *
import numpy as np

class RelationsAndFunctions(Scene):
    def construct(self):
        # Title sequence
        title = Text("Relations and Functions", font_size=60)
        subtitle = Text("A Visual Guide", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title_group))
        
        # Part 1: Relations Introduction
        relations_title = Text("Relations", font_size=48)
        relations_title.to_edge(UP)
        
        self.play(Write(relations_title))
        
        # Visualize a relation as a mapping between sets
        set_a = Circle(radius=1.5, color=BLUE)
        set_a.shift(LEFT * 3)
        set_a_label = Text("Set A", font_size=28).next_to(set_a, UP)
        
        set_b = Circle(radius=1.5, color=RED)
        set_b.shift(RIGHT * 3)
        set_b_label = Text("Set B", font_size=28).next_to(set_b, UP)
        
        self.play(
            Create(set_a),
            Write(set_a_label),
            Create(set_b),
            Write(set_b_label)
        )
        
        # Create elements in set A
        points_a = [
            set_a.point_from_proportion(i/3) for i in range(3)
        ]
        dots_a = [Dot(point, color=BLUE_E) for point in points_a]
        labels_a = [
            Text(f"a{i+1}", font_size=24).next_to(dots_a[i], LEFT*0.5) 
            for i in range(3)
        ]
        
        # Create elements in set B
        points_b = [
            set_b.point_from_proportion(i/4) for i in range(4)
        ]
        dots_b = [Dot(point, color=RED_E) for point in points_b]
        labels_b = [
            Text(f"b{i+1}", font_size=24).next_to(dots_b[i], RIGHT*0.5) 
            for i in range(4)
        ]
        
        self.play(
            *[Create(dot) for dot in dots_a],
            *[Write(label) for label in labels_a],
            *[Create(dot) for dot in dots_b],
            *[Write(label) for label in labels_b]
        )
        
        # Definition of a relation
        relation_def = Text("A relation R from set A to set B is a subset of A × B", font_size=32)
        relation_def.next_to(relations_title, DOWN, buff=0.5)
        
        self.play(Write(relation_def))
        self.wait(1)
        
        # Show some arrows to represent a relation
        arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=YELLOW),
            Arrow(dots_a[0].get_center(), dots_b[2].get_center(), color=YELLOW),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=YELLOW),
            Arrow(dots_a[2].get_center(), dots_b[3].get_center(), color=YELLOW)
        ]
        
        self.play(*[Create(arrow) for arrow in arrows])
        
        # Explain domain, codomain, range
        domain_def = Text("Domain: Set of all first elements in the relation", font_size=28)
        codomain_def = Text("Codomain: The target set B", font_size=28)
        range_def = Text("Range: Set of all second elements in the relation", font_size=28)
        
        domain_def.next_to(relation_def, DOWN, buff=0.4)
        codomain_def.next_to(domain_def, DOWN, buff=0.2)
        range_def.next_to(codomain_def, DOWN, buff=0.2)
        
        self.play(Write(domain_def))
        self.play(Write(codomain_def))
        self.play(Write(range_def))
        
        self.wait(1)
        
        # Clear the screen for properties
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Part 2: Properties of Relations
        properties_title = Text("Properties of Relations", font_size=48)
        properties_title.to_edge(UP)
        
        self.play(Write(properties_title))
        
        # Create a simpler relation on a single set for demonstrating properties
        set_c = Circle(radius=2, color=GREEN)
        set_c_label = Text("Set C", font_size=28).next_to(set_c, UP)
        
        self.play(
            Create(set_c),
            Write(set_c_label)
        )
        
        # Create elements in set C
        points_c = [
            set_c.point_from_proportion(i/4) for i in range(4)
        ]
        dots_c = [Dot(point, color=GREEN_E) for point in points_c]
        labels_c = [
            Text(f"c{i+1}", font_size=24).next_to(dots_c[i], 
                                                 dots_c[i].get_center() - set_c.get_center()) 
            for i in range(4)
        ]
        
        self.play(
            *[Create(dot) for dot in dots_c],
            *[Write(label) for label in labels_c]
        )
        
        # Reflexive property
        reflexive_title = Text("Reflexive Property", font_size=32, color=YELLOW)
        reflexive_title.next_to(properties_title, DOWN, buff=0.5)
        reflexive_def = Text("(a, a) ∈ R for all a ∈ A", font_size=24)
        reflexive_def.next_to(reflexive_title, DOWN, buff=0.3)
        
        self.play(Write(reflexive_title))
        self.play(Write(reflexive_def))
        
        # Show reflexive property with loops
        reflexive_arrows = [
            CurvedArrow(
                start_point=dots_c[i].get_center() + UP*0.3,
                end_point=dots_c[i].get_center() + RIGHT*0.3,
                angle=-TAU/4,
                color=YELLOW
            ) for i in range(4)
        ]
        
        self.play(*[Create(arrow) for arrow in reflexive_arrows])
        self.wait(1)
        
        # Symmetric property
        symmetric_title = Text("Symmetric Property", font_size=32, color=BLUE)
        symmetric_title.next_to(properties_title, DOWN, buff=0.5)
        symmetric_def = Text("If (a, b) ∈ R, then (b, a) ∈ R", font_size=24)
        symmetric_def.next_to(symmetric_title, DOWN, buff=0.3)
        
        self.play(
            FadeOut(reflexive_title),
            FadeOut(reflexive_def),
            *[FadeOut(arrow) for arrow in reflexive_arrows],
            Write(symmetric_title),
            Write(symmetric_def)
        )
        
        # Show symmetric property with bidirectional arrows
        symmetric_arrows1 = [
            Arrow(dots_c[0].get_center(), dots_c[1].get_center(), color=BLUE),
            Arrow(dots_c[2].get_center(), dots_c[3].get_center(), color=BLUE)
        ]
        
        symmetric_arrows2 = [
            Arrow(dots_c[1].get_center(), dots_c[0].get_center(), color=BLUE),
            Arrow(dots_c[3].get_center(), dots_c[2].get_center(), color=BLUE)
        ]
        
        self.play(*[Create(arrow) for arrow in symmetric_arrows1])
        self.play(*[Create(arrow) for arrow in symmetric_arrows2])
        self.wait(1)
        
        # Transitive property
        transitive_title = Text("Transitive Property", font_size=32, color=PURPLE)
        transitive_title.next_to(properties_title, DOWN, buff=0.5)
        transitive_def = Text("If (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R", font_size=24)
        transitive_def.next_to(transitive_title, DOWN, buff=0.3)
        
        self.play(
            FadeOut(symmetric_title),
            FadeOut(symmetric_def),
            *[FadeOut(arrow) for arrow in symmetric_arrows1 + symmetric_arrows2],
            Write(transitive_title),
            Write(transitive_def)
        )
        
        # Show transitive property with arrows
        transitive_arrows1 = [
            Arrow(dots_c[0].get_center(), dots_c[1].get_center(), color=PURPLE),
            Arrow(dots_c[1].get_center(), dots_c[2].get_center(), color=PURPLE)
        ]
        
        transitive_arrows2 = [
            Arrow(dots_c[0].get_center(), dots_c[2].get_center(), color=RED)
        ]
        
        self.play(*[Create(arrow) for arrow in transitive_arrows1])
        self.play(*[Create(arrow) for arrow in transitive_arrows2])
        self.wait(1)
        
        # Equivalence relation
        equivalence_title = Text("Equivalence Relation", font_size=32, color=ORANGE)
        equivalence_def = Text("A relation that is reflexive, symmetric, and transitive", font_size=24)
        equivalence_title.next_to(properties_title, DOWN, buff=0.5)
        equivalence_def.next_to(equivalence_title, DOWN, buff=0.3)
        
        self.play(
            FadeOut(transitive_title),
            FadeOut(transitive_def),
            *[FadeOut(arrow) for arrow in transitive_arrows1 + transitive_arrows2],
            Write(equivalence_title),
            Write(equivalence_def)
        )
        
        # Show equivalence relation with partitions
        self.play(
            FadeOut(set_c),
            FadeOut(set_c_label),
            *[FadeOut(dot) for dot in dots_c],
            *[FadeOut(label) for label in labels_c],
        )
        
        # Equivalence classes
        eq_class_title = Text("Equivalence Classes", font_size=32, color=ORANGE)
        eq_class_title.next_to(equivalence_def, DOWN, buff=0.5)
        
        self.play(Write(eq_class_title))
        
        # Create partitions for equivalence classes
        partition1 = Circle(radius=1.2, color=ORANGE)
        partition1.shift(LEFT * 2.5)
        partition1_label = Text("[a]", font_size=28).next_to(partition1, UP)
        
        partition2 = Circle(radius=1.2, color=ORANGE)
        partition2.shift(RIGHT * 2.5)
        partition2_label = Text("[b]", font_size=28).next_to(partition2, UP)
        
        self.play(
            Create(partition1),
            Write(partition1_label),
            Create(partition2),
            Write(partition2_label)
        )
        
        # Fill in elements in partitions
        elements1 = VGroup(
            Dot(partition1.get_center() + UP*0.5, color=ORANGE),
            Dot(partition1.get_center() + LEFT*0.5, color=ORANGE),
            Dot(partition1.get_center() + DOWN*0.5, color=ORANGE)
        )
        
        elements2 = VGroup(
            Dot(partition2.get_center() + UP*0.5, color=ORANGE),
            Dot(partition2.get_center() + RIGHT*0.5, color=ORANGE),
            Dot(partition2.get_center() + DOWN*0.5, color=ORANGE)
        )
        
        self.play(
            Create(elements1),
            Create(elements2)
        )
        
        partition_text = Text("Equivalence classes form a partition of the set", font_size=24)
        partition_text.next_to(eq_class_title, DOWN, buff=0.5)
        
        self.play(Write(partition_text))
        self.wait(1)
        
        # Clear the screen for Functions
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Part 3: Functions
        functions_title = Text("Functions", font_size=48)
        functions_title.to_edge(UP)
        
        self.play(Write(functions_title))
        
        # Definition of a function
        function_def = Text("A function f: A → B is a relation where each element in A", font_size=28)
        function_def2 = Text("is related to exactly one element in B", font_size=28)
        function_def.next_to(functions_title, DOWN, buff=0.5)
        function_def2.next_to(function_def, DOWN, buff=0.2)
        
        self.play(Write(function_def), Write(function_def2))
        
        # Visualize a function with sets
        set_a = Circle(radius=1.5, color=BLUE)
        set_a.shift(LEFT * 3)
        set_a_label = Text("Set A", font_size=28).next_to(set_a, UP)
        
        set_b = Circle(radius=1.5, color=RED)
        set_b.shift(RIGHT * 3)
        set_b_label = Text("Set B", font_size=28).next_to(set_b, UP)
        
        self.play(
            Create(set_a),
            Write(set_a_label),
            Create(set_b),
            Write(set_b_label)
        )
        
        # Create elements in set A
        points_a = [
            set_a.point_from_proportion(i/3) for i in range(3)
        ]
        dots_a = [Dot(point, color=BLUE_E) for point in points_a]
        labels_a = [
            Text(f"a{i+1}", font_size=24).next_to(dots_a[i], LEFT*0.5) 
            for i in range(3)
        ]
        
        # Create elements in set B
        points_b = [
            set_b.point_from_proportion(i/3) for i in range(3)
        ]
        dots_b = [Dot(point, color=RED_E) for point in points_b]
        labels_b = [
            Text(f"b{i+1}", font_size=24).next_to(dots_b[i], RIGHT*0.5) 
            for i in range(3)
        ]
        
        self.play(
            *[Create(dot) for dot in dots_a],
            *[Write(label) for label in labels_a],
            *[Create(dot) for dot in dots_b],
            *[Write(label) for label in labels_b]
        )
        
        # Show function mapping with arrows
        function_arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=YELLOW),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=YELLOW),
            Arrow(dots_a[2].get_center(), dots_b[2].get_center(), color=YELLOW)
        ]
        
        self.play(*[Create(arrow) for arrow in function_arrows])
        self.wait(1)
        
        # Clear for the types of functions
        self.play(
            FadeOut(function_def),
            FadeOut(function_def2),
            *[FadeOut(arrow) for arrow in function_arrows]
        )
        
        # Types of functions
        function_types = Text("Types of Functions", font_size=32)
        function_types.next_to(functions_title, DOWN, buff=0.5)
        
        self.play(Write(function_types))
        
        # One-to-one (Injective)
        injective_title = Text("One-One (Injective)", font_size=28, color=YELLOW)
        injective_title.next_to(function_types, DOWN, buff=0.5)
        injective_def = Text("f(x₁) = f(x₂) ⟹ x₁ = x₂", font_size=24)
        injective_def2 = Text("Different inputs → Different outputs", font_size=24)
        injective_def.next_to(injective_title, DOWN, buff=0.3)
        injective_def2.next_to(injective_def, DOWN, buff=0.2)
        
        self.play(Write(injective_title))
        self.play(Write(injective_def), Write(injective_def2))
        
        # Show injective function
        injective_arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=YELLOW),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=YELLOW),
            Arrow(dots_a[2].get_center(), dots_b[2].get_center(), color=YELLOW)
        ]
        
        self.play(*[Create(arrow) for arrow in injective_arrows])
        self.wait(1)
        
        # Onto (Surjective)
        surjective_title = Text("Onto (Surjective)", font_size=28, color=GREEN)
        surjective_title.next_to(function_types, DOWN, buff=0.5)
        surjective_def = Text("For every y ∈ B, there exists x ∈ A such that f(x) = y", font_size=24)
        surjective_def2 = Text("All outputs are covered", font_size=24)
        surjective_def.next_to(surjective_title, DOWN, buff=0.3)
        surjective_def2.next_to(surjective_def, DOWN, buff=0.2)
        
        self.play(
            FadeOut(injective_title),
            FadeOut(injective_def),
            FadeOut(injective_def2),
            *[FadeOut(arrow) for arrow in injective_arrows],
            Write(surjective_title),
            Write(surjective_def),
            Write(surjective_def2)
        )
        
        # Show surjective function
        surjective_arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=GREEN),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=GREEN),
            Arrow(dots_a[2].get_center(), dots_b[2].get_center(), color=GREEN)
        ]
        
        self.play(*[Create(arrow) for arrow in surjective_arrows])
        self.wait(1)
        
        # Bijective
        bijective_title = Text("Bijective", font_size=28, color=PURPLE)
        bijective_title.next_to(function_types, DOWN, buff=0.5)
        bijective_def = Text("Both one-one and onto", font_size=24)
        bijective_def.next_to(bijective_title, DOWN, buff=0.3)
        
        self.play(
            FadeOut(surjective_title),
            FadeOut(surjective_def),
            FadeOut(surjective_def2),
            *[FadeOut(arrow) for arrow in surjective_arrows],
            Write(bijective_title),
            Write(bijective_def)
        )
        
        # Show bijective function
        bijective_arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=PURPLE),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=PURPLE),
            Arrow(dots_a[2].get_center(), dots_b[2].get_center(), color=PURPLE)
        ]
        
        self.play(*[Create(arrow) for arrow in bijective_arrows])
        self.wait(1)
        
        # Important theorem for finite sets
        theorem = Text("For finite sets of equal size, a function is", font_size=24)
        theorem2 = Text("one-one if and only if it is onto", font_size=24)
        theorem.next_to(bijective_def, DOWN, buff=0.5)
        theorem2.next_to(theorem, DOWN, buff=0.2)
        
        self.play(Write(theorem), Write(theorem2))
        self.wait(1)
        
        # Clear for function operations
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Part 4: Function Operations
        operations_title = Text("Function Operations", font_size=48)
        operations_title.to_edge(UP)
        
        self.play(Write(operations_title))
        
        # Function Composition
        composition_title = Text("Composition of Functions", font_size=32)
        composition_title.next_to(operations_title, DOWN, buff=0.5)
        
        composition_def = Text("(g ∘ f)(x) = g(f(x))", font_size=28)
        composition_def.next_to(composition_title, DOWN, buff=0.3)
        
        self.play(Write(composition_title))
        self.play(Write(composition_def))
        
        # Visualize function composition
        set_a = Circle(radius=1.2, color=BLUE)
        set_a.shift(LEFT * 4)
        set_a_label = Text("Set A", font_size=24).next_to(set_a, UP)
        
        set_b = Circle(radius=1.2, color=GREEN)
        set_b_label = Text("Set B", font_size=24).next_to(set_b, UP)
        
        set_c = Circle(radius=1.2, color=RED)
        set_c.shift(RIGHT * 4)
        set_c_label = Text("Set C", font_size=24).next_to(set_c, UP)
        
        self.play(
            Create(set_a),
            Write(set_a_label),
            Create(set_b),
            Write(set_b_label),
            Create(set_c),
            Write(set_c_label)
        )
        
        # Create elements in sets
        points_a = [set_a.point_from_proportion(i/2) for i in range(2)]
        dots_a = [Dot(point, color=BLUE_E) for point in points_a]
        labels_a = [Text(f"a{i+1}", font_size=20).next_to(dots_a[i], LEFT*0.5) for i in range(2)]
        
        points_b = [set_b.point_from_proportion(i/2) for i in range(2)]
        dots_b = [Dot(point, color=GREEN_E) for point in points_b]
        labels_b = [Text(f"b{i+1}", font_size=20) for i in range(2)]
        labels_b[0].next_to(dots_b[0], UP*0.5)
        labels_b[1].next_to(dots_b[1], DOWN*0.5)
        
        points_c = [set_c.point_from_proportion(i/2) for i in range(2)]
        dots_c = [Dot(point, color=RED_E) for point in points_c]
        labels_c = [Text(f"c{i+1}", font_size=20).next_to(dots_c[i], RIGHT*0.5) for i in range(2)]
        
        self.play(
            *[Create(dot) for dot in dots_a + dots_b + dots_c],
            *[Write(label) for label in labels_a + labels_b + labels_c]
        )
        
        # Function f arrows
        f_arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=BLUE),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=BLUE)
        ]
        f_label = Text("f", font_size=24, color=BLUE).move_to(
            (set_a.get_center() + set_b.get_center()) / 2 + UP*1.5
        )
        
        # Function g arrows
        g_arrows = [
            Arrow(dots_b[0].get_center(), dots_c[0].get_center(), color=GREEN),
            Arrow(dots_b[1].get_center(), dots_c[1].get_center(), color=GREEN)
        ]
        g_label = Text("g", font_size=24, color=GREEN).move_to(
            (set_b.get_center() + set_c.get_center()) / 2 + UP*1.5
        )
        
        # Composition arrows
        gof_arrows = [
            CurvedArrow(
                start_point=dots_a[0].get_center(),
                end_point=dots_c[0].get_center(),
                angle=0.4,
                color=PURPLE
            ),
            CurvedArrow(
                start_point=dots_a[1].get_center(),
                end_point=dots_c[1].get_center(),
                angle=0.4,
                color=PURPLE
            )
        ]
        gof_label = Text("g ∘ f", font_size=24, color=PURPLE).move_to(
            (set_a.get_center() + set_c.get_center()) / 2 + DOWN*1.5
        )
        
        # Show f first
        self.play(
            *[Create(arrow) for arrow in f_arrows],
            Write(f_label)
        )
        
        # Then show g
        self.play(
            *[Create(arrow) for arrow in g_arrows],
            Write(g_label)
        )
        
        # Finally show composition
        self.play(
            *[Create(arrow) for arrow in gof_arrows],
            Write(gof_label)
        )
        
        self.wait(1)
        
        # Clear for invertible functions
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Part 5: Invertible Functions
        invertible_title = Text("Invertible Functions", font_size=48)
        invertible_title.to_edge(UP)
        
        self.play(Write(invertible_title))
        
        invertible_def = Text("A function with an inverse function f⁻¹ where", font_size=28)
        invertible_def2 = Text("f⁻¹∘f = I_A and f∘f⁻¹ = I_B", font_size=28)
        invertible_def.next_to(invertible_title, DOWN, buff=0.5)
        invertible_def2.next_to(invertible_def, DOWN, buff=0.2)
        
        self.play(Write(invertible_def), Write(invertible_def2))
        
        condition = Text("A function is invertible if and only if it is bijective", font_size=28, color=YELLOW)
        condition.next_to(invertible_def2, DOWN, buff=0.5)
        
        self.play(Write(condition))
        
        # Visualize invertible function
        set_a = Circle(radius=1.5, color=BLUE)
        set_a.shift(LEFT * 3)
        set_a_label = Text("Set A", font_size=28).next_to(set_a, UP)
        
        set_b = Circle(radius=1.5, color=RED)
        set_b.shift(RIGHT * 3)
        set_b_label = Text("Set B", font_size=28).next_to(set_b, UP)
        
        self.play(
            Create(set_a),
            Write(set_a_label),
            Create(set_b),
            Write(set_b_label)
        )
        
        # Create elements in sets
        points_a = [set_a.point_from_proportion(i/3) for i in range(3)]
        dots_a = [Dot(point, color=BLUE_E) for point in points_a]
        labels_a = [Text(f"a{i+1}", font_size=24).next_to(dots_a[i], LEFT*0.5) for i in range(3)]
        
        points_b = [set_b.point_from_proportion(i/3) for i in range(3)]
        dots_b = [Dot(point, color=RED_E) for point in points_b]
        labels_b = [Text(f"b{i+1}", font_size=24).next_to(dots_b[i], RIGHT*0.5) for i in range(3)]
        
        self.play(
            *[Create(dot) for dot in dots_a + dots_b],
            *[Write(label) for label in labels_a + labels_b]
        )
        
        # Function f arrows
        f_arrows = [
            Arrow(dots_a[0].get_center(), dots_b[0].get_center(), color=BLUE),
            Arrow(dots_a[1].get_center(), dots_b[1].get_center(), color=BLUE),
            Arrow(dots_a[2].get_center(), dots_b[2].get_center(), color=BLUE)
        ]
        f_label = Text("f", font_size=24, color=BLUE).move_to(
            (set_a.get_center() + set_b.get_center()) / 2 + UP*1.5
        )
        
        # Function f^(-1) arrows
        f_inv_arrows = [
            Arrow(dots_b[0].get_center(), dots_a[0].get_center(), color=RED),
            Arrow(dots_b[1].get_center(), dots_a[1].get_center(), color=RED),
            Arrow(dots_b[2].get_center(), dots_a[2].get_center(), color=RED)
        ]
        f_inv_label = Text("f⁻¹", font_size=24, color=RED).move_to(
            (set_a.get_center() + set_b.get_center()) / 2 + DOWN*1.5
        )
        
        # Show f first
        self.play(
            *[Create(arrow) for arrow in f_arrows],
            Write(f_label)
        )
        
        # Then show f^(-1)
        self.play(
            *[Create(arrow) for arrow in f_inv_arrows],
            Write(f_inv_label)
        )
        
        # Example of inverse function
        example = Text("Example: f(x) = 2x + 3", font_size=24)
        example.next_to(set_b, DOWN, buff=1.0)
        
        inverse = Text("Inverse: f⁻¹(y) = (y-3)/2", font_size=24)
        inverse.next_to(example, DOWN, buff=0.3)
        
        self.play(Write(example), Write(inverse))
        self.wait(1)
        
        # Final recap
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Conclusion with key takeaways
        final_title = Text("Key Takeaways", font_size=48)
        final_title.to_edge(UP)
        
        self.play(Write(final_title))
        
        takeaways = [
            Text("• A relation is a subset of A × B", font_size=28),
            Text("• Relations can be reflexive, symmetric, transitive", font_size=28),
            Text("• An equivalence relation partitions a set", font_size=28),
            Text("• A function maps each input to exactly one output", font_size=28),
            Text("• Functions can be injective, surjective, or bijective", font_size=28),
            Text("• A function is invertible if and only if it is bijective", font_size=28)
        ]
        
        for i, takeaway in enumerate(takeaways):
            takeaway.next_to(final_title, DOWN, buff=0.5 + i*0.6)
            self.play(Write(takeaway))
        
        self.wait(2)
        
        # Fade out everything
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # End title
        end_title = Text("Relations and Functions", font_size=60)
        end_subtitle = Text("A Visual Guide", font_size=36)
        end_subtitle.next_to(end_title, DOWN, buff=0.5)
        
        self.play(Write(end_title))
        self.play(FadeIn(end_subtitle))
        self.wait(2)
        
        self.play(
            FadeOut(end_title),
            FadeOut(end_subtitle)
        )


class RelationsExamples(Scene):
    def construct(self):
        # Title
        title = Text("Relations and Functions", font_size=60)
        subtitle = Text("Real-world Examples", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Example 1: Equivalence Relation
        eq_title = Text("Equivalence Relation Example: Congruence Modulo n", font_size=36)
        eq_title.to_edge(UP)
        
        self.play(Write(eq_title))
        
        eq_def = Text("a ≡ b (mod n) if n divides (a-b)", font_size=28)
        eq_def.next_to(eq_title, DOWN, buff=0.5)
        
        self.play(Write(eq_def))
        
        # Visualize equivalence classes modulo 3
        mod3_title = Text("Equivalence Classes Modulo 3", font_size=32)
        mod3_title.next_to(eq_def, DOWN, buff=0.5)
        
        self.play(Write(mod3_title))
        
        # Create circles for each equivalence class
        class0 = Circle(radius=1.2, color=BLUE)
        class0.shift(LEFT * 3)
        class0_label = Text("[0]₃", font_size=28).next_to(class0, UP)
        
        class1 = Circle(radius=1.2, color=GREEN)
        class1_label = Text("[1]₃", font_size=28).next_to(class1, UP)
        
        class2 = Circle(radius=1.2, color=RED)
        class2.shift(RIGHT * 3)
        class2_label = Text("[2]₃", font_size=28).next_to(class2, UP)
        
        self.play(
            Create(class0),
            Write(class0_label),
            Create(class1),
            Write(class1_label),
            Create(class2),
            Write(class2_label)
        )
        
        # Add elements to each class
        class0_elements = VGroup(
            Text("0", font_size=24),
            Text("3", font_size=24),
            Text("6", font_size=24),
            Text("...", font_size=24)
        ).arrange(DOWN, buff=0.2).move_to(class0)
        
        class1_elements = VGroup(
            Text("1", font_size=24),
            Text("4", font_size=24),
            Text("7", font_size=24),
            Text("...", font_size=24)
        ).arrange(DOWN, buff=0.2).move_to(class1)
        
        class2_elements = VGroup(
            Text("2", font_size=24),
            Text("5", font_size=24),
            Text("8", font_size=24),
            Text("...", font_size=24)
        ).arrange(DOWN, buff=0.2).move_to(class2)
        
        self.play(
            Write(class0_elements),
            Write(class1_elements),
            Write(class2_elements)
        )
        
        # Show properties
        properties = Text("This relation is reflexive, symmetric, and transitive", font_size=28)
        properties.next_to(mod3_title, DOWN, buff=2.5)
        
        self.play(Write(properties))
        self.wait(1)
        
        # Clear screen
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Example 2: Function Types
        func_title = Text("Function Example: f(x) = 2x", font_size=36)
        func_title.to_edge(UP)
        
        self.play(Write(func_title))
        
        # Create three versions of the function
        nat_title = Text("f: N → N (one-one but not onto)", font_size=28, color=BLUE)
        nat_title.next_to(func_title, DOWN, buff=0.5)
        
        real_title = Text("f: R → R (one-one and onto / bijective)", font_size=28, color=GREEN)
        real_title.next_to(nat_title, DOWN, buff=0.3)
        
        self.play(Write(nat_title))
        self.play(Write(real_title))
        
        # Create coordinate system for N to N
        n_to_n = NumberPlane(
            x_range=[-1, 11, 1],
            y_range=[-1, 21, 2],
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        n_to_n.shift(LEFT * 3 + DOWN * 1)
        
        # Add axes labels
        n_to_n_x_label = Text("N", font_size=20).next_to(n_to_n, DOWN)
        n_to_n_y_label = Text("N", font_size=20).next_to(n_to_n, LEFT)
        
        self.play(
            Create(n_to_n),
            Write(n_to_n_x_label),
            Write(n_to_n_y_label)
        )
        
        # Create coordinate system for R to R
        r_to_r = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-10, 10, 2],
            x_length=4,
            y_length=4,
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        r_to_r.shift(RIGHT * 3 + DOWN * 1)
        
        # Add axes labels
        r_to_r_x_label = Text("R", font_size=20).next_to(r_to_r, DOWN)
        r_to_r_y_label = Text("R", font_size=20).next_to(r_to_r, LEFT)
        
        self.play(
            Create(r_to_r),
            Write(r_to_r_x_label),
            Write(r_to_r_y_label)
        )
        
        # Plot f(x) = 2x for natural numbers
        nat_dots = VGroup()
        for i in range(1, 6):
            nat_dots.add(Dot(n_to_n.c2p(i, 2*i), color=BLUE))
        
        self.play(Create(nat_dots))
        
        # Highlight that 3 has no preimage
        missing_point = Dot(n_to_n.c2p(0, 3), color=RED)
        missing_label = Text("3 has no preimage", font_size=16).next_to(missing_point, RIGHT, buff=0.2)
        
        self.play(Create(missing_point), Write(missing_label))
        
        # Plot f(x) = 2x for real numbers
        real_graph = r_to_r.plot(lambda x: 2*x, x_range=[-5, 5], color=GREEN)
        
        self.play(Create(real_graph))
        
        # Show that every number has a preimage
        bijective_text = Text("Every y has a preimage x = y/2", font_size=16)
        bijective_text.next_to(r_to_r, UP, buff=0.3)
        
        self.play(Write(bijective_text))
        
        # Example point and its preimage
        point_y = 4
        point_x = point_y / 2
        
        point = Dot(r_to_r.c2p(point_x, point_y), color=YELLOW)
        point_label = Text("(2, 4)", font_size=16).next_to(point, UP, buff=0.2)
        
        self.play(Create(point), Write(point_label))
        
        self.wait(1)
        
        # Clear for final example
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Function Composition Example
        comp_title = Text("Function Composition Example", font_size=36)
        comp_title.to_edge(UP)
        
        self.play(Write(comp_title))
        
        comp_ex = Text("f(x) = x² and g(x) = x + 3", font_size=28)
        comp_ex.next_to(comp_title, DOWN, buff=0.5)
        
        self.play(Write(comp_ex))
        
        comp_result1 = Text("(g ∘ f)(x) = g(f(x)) = g(x²) = x² + 3", font_size=28)
        comp_result2 = Text("(f ∘ g)(x) = f(g(x)) = f(x + 3) = (x + 3)²", font_size=28)
        
        comp_result1.next_to(comp_ex, DOWN, buff=0.5)
        comp_result2.next_to(comp_result1, DOWN, buff=0.3)
        
        self.play(Write(comp_result1))
        self.play(Write(comp_result2))
        
        comp_note = Text("Notice: g ∘ f ≠ f ∘ g (composition is not commutative)", font_size=28, color=YELLOW)
        comp_note.next_to(comp_result2, DOWN, buff=0.5)
        
        self.play(Write(comp_note))
        
        # Create graphs to compare
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 12, 2],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        )
        axes.shift(DOWN * 1)
        
        # Add axes labels
        axes_labels = axes.get_axis_labels("x", "y")
        
        self.play(
            Create(axes),
            Write(axes_labels)
        )
        
        # Plot (g ∘ f)(x) = x² + 3
        gof_graph = axes.plot(lambda x: x**2 + 3, x_range=[-3, 3], color=BLUE)
        gof_label = Text("g ∘ f", font_size=24, color=BLUE).next_to(gof_graph, UP)
        
        # Plot (f ∘ g)(x) = (x + 3)²
        fog_graph = axes.plot(lambda x: (x + 3)**2, x_range=[-3, 3], color=RED)
        fog_label = Text("f ∘ g", font_size=24, color=RED).next_to(fog_graph, RIGHT)
        
        self.play(
            Create(gof_graph),
            Write(gof_label)
        )
        
        self.play(
            Create(fog_graph),
            Write(fog_label)
        )
        
        self.wait(2)
        
        # Final farewell
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        thanks = Text("Thank you for watching!", font_size=48)
        
        self.play(Write(thanks))
        self.wait(2)
        
        self.play(FadeOut(thanks))


# Extended class for specific examples if needed
class FunctionInvertibility(Scene):
    def construct(self):
        title = Text("Function Invertibility", font_size=48)
        title.to_edge(UP)
        
        self.play(Write(title))
        
        # Create a simple function example
        function_ex = Text("Example: f(x) = x² for x ≥ 0", font_size=32)
        function_ex.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(function_ex))
        
        # Set up axes
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 10, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": False}
        )
        axes.shift(DOWN * 0.5)
        
        # Add axes labels
        axes_labels = axes.get_axis_labels("x", "y")
        
        self.play(
            Create(axes),
            Write(axes_labels)
        )
        
        # Plot f(x) = x²
        restricted_graph = axes.plot(lambda x: x**2, x_range=[0, 4], color=BLUE)
        graph_label = Text("f(x) = x²", font_size=24, color=BLUE).next_to(restricted_graph, UP)
        
        self.play(
            Create(restricted_graph),
            Write(graph_label)
        )
        
        # Explain invertibility
        note = Text("This function is invertible on its restricted domain", font_size=24)
        note.next_to(axes, DOWN, buff=0.5)
        
        self.play(Write(note))
        
        # Show the inverse function
        inverse_graph = axes.plot(lambda x: np.sqrt(x), x_range=[0, 9], color=RED)
        inverse_label = Text("f⁻¹(x) = √x", font_size=24, color=RED).next_to(inverse_graph, RIGHT)
        
        self.play(
            Create(inverse_graph),
            Write(inverse_label)
        )
        
        # Demonstrate composition
        composition_note = Text("f⁻¹(f(x)) = √(x²) = x for x ≥ 0", font_size=24)
        composition_note2 = Text("f(f⁻¹(x)) = (√x)² = x for x ≥ 0", font_size=24)
        
        composition_note.next_to(note, DOWN, buff=0.3)
        composition_note2.next_to(composition_note, DOWN, buff=0.3)
        
        self.play(Write(composition_note))
        self.play(Write(composition_note2))
        
        self.wait(2)
        
        # Fade out everything
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )


# This is the main class that combines all the scenes together
class RelationsAndFunctionsVideo(Scene):
    def construct(self):
        # Start with a title screen
        title = Text("Relations and Functions", font_size=60)
        subtitle = Text("A Visual Guide", font_size=36)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        
        # Introduce the outline
        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )
        
        outline_title = Text("Outline", font_size=48)
        outline_title.to_edge(UP)
        
        self.play(Write(outline_title))
        
        # Create outline items
        outline_items = VGroup(
            Text("1. Relations", font_size=36),
            Text("2. Properties of Relations", font_size=36),
            Text("3. Equivalence Relations", font_size=36),
            Text("4. Functions", font_size=36),
            Text("5. Types of Functions", font_size=36),
            Text("6. Function Operations", font_size=36),
            Text("7. Invertible Functions", font_size=36)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        outline_items.next_to(outline_title, DOWN, buff=0.5)
        
        self.play(Write(outline_items))
        self.wait(2)
        
        # Transition to the first scene
        self.play(
            *[FadeOut(obj) for obj in self.mobjects]
        )
        
        # Instance of the RelationsAndFunctions class
        relations_and_functions = RelationsAndFunctions()
        
        # Run the scene
        relations_and_functions.construct()
        
        # End with a thank you message
        thanks = Text("Thank you for watching!", font_size=48)
        
        self.play(Write(thanks))
        self.wait(2)
        
        self.play(FadeOut(thanks))


if __name__ == "__main__":
    # This is the main entry point when running the script
    # You can choose which scene to render by uncommenting the appropriate line
    
    # For the complete video
    module_name = "RelationsAndFunctionsVideo"
    
    # For individual sections
    # module_name = "RelationsAndFunctions"
    # module_name = "RelationsExamples"
    # module_name = "FunctionInvertibility"