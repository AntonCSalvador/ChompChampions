class Champions:

    def __init__(self, speed, hit_box, strength, weight, resistance):
        self.speed = speed
        self.default_speed = speed
        self.hit_box = hit_box
        self.strength = strength
        self.default_strength = strength
        self.weight = weight
        self.resistance = resistance

    def update_speed(self, speed_multiplier):
        self.speed = self.speed * speed_multiplier

    def reset_speed(self):
        self.speed = self.default_speed

    def update_strength(self, strength_multiplier):
        self.strength = self.strength * strength_multiplier

    def reset_speed(self):
        self.strength = self.default_strength

    # def update_
