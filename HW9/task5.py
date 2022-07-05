class Stationary:
    def __init__(self, title="Something that can draw"):
        self.title = title
    def draw(self):
        print(f"Start drawing! {self.title}:")

class Pen(Stationary):
    def draw(self):
        print(f"Drawing with {self.title} pen!")

class Pencil(Stationary):
    def draw(self):
        print(f"Drawing with {self.title} pencil!")

class Marker(Stationary):
    def draw(self):
        print(f"Drawing with {self.title} marker!")

start = Stationary()
pen = Pen("BIG")
pencil = Pencil("KOH-I-NOOR")
marker = Marker("Permanent")

office_suppliers = [start, pen, pencil, marker]

for i in office_suppliers:
    i.draw()
