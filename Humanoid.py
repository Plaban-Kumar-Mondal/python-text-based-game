class Humanoid:
    def __init__(self, health, attack_damage):
        self.health = health
        self.current_health = self.health
        self.attack_damage = attack_damage

    def _clamp(self, minimum, x, maximum):
        return max(minimum, min(x, maximum))

    def hurt(self, amount):
        self.current_health -= amount
        return self._clamp(0, self.current_health, self.health)
