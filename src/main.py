from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from BlobHandler import BlobHandler
from FoodHandler import FoodHandler
from rich.text import Text
from constants import INITIAL_BLOBS, INITIAL_FOOD, BLOB_DIRS, FOOD, EMPTY, WIDTH, HEIGHT, UPDATE_RATE

class NeuroEvolve(App):

    CSS = """
        Static {
            width: 100%;
            height: 100%;
            content-align: center middle;
        }

        #grid {
            layout: grid;
            grid-size: 25 25;
            grid-gutter: 0;
        }
    """

    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(id="grid")
        yield Footer()

    def on_mount(self) -> None:
        self.blobHandler = BlobHandler()
        self.foodHandler = FoodHandler(self.blobHandler)
        self.blobHandler.foodHandler = self.foodHandler

        for i in range(INITIAL_BLOBS):
            self.blobHandler.new_blob()
        
        for i in range(INITIAL_FOOD):
            self.foodHandler.new_food()


        grid = self.query_one("#grid", Container)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                grid.mount(Static(EMPTY, id=f"cell_{x}_{y}"))

        self.render_grid()

        self.set_interval(UPDATE_RATE, self.update_sim)

    def render_grid(self) -> None:
        blob_positions = {b.pos: [BLOB_DIRS[b.facing], b.color] for b in self.blobHandler.get_blobs()}
        food_positions = self.foodHandler.get_food_positions()

        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = (x, y)
                cell = self.query_one(f"#cell_{x}_{y}", Static)

                if pos in blob_positions:
                    symbol, color = blob_positions[pos]
                    text = Text(symbol)
                    text.stylize(f"rgb({str(color[0])},{str(color[1])},{str(color[2])})")
                    cell.update(text)
                elif pos in food_positions:
                    text = Text(FOOD)
                    text.stylize("rgb(0,255,0)")
                    cell.update(text)
                else:
                    cell.update(EMPTY)
                    cell.remove_class(*cell.classes)

    def update_sim(self) -> None:
        food_consumed = self.blobHandler.update()
        for food in food_consumed:
            self.foodHandler.remove_food(food)
        self.foodHandler.spawn_food()
        self.blobHandler.check_deaths()
        self.blobHandler.check_reproduction()
        self.render_grid()

    def quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = NeuroEvolve()
    app.run()