from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from BlobHandler import BlobHandler
from rich.text import Text
from constants import BLOB_DIRS, FOOD, EMPTY, WIDTH, HEIGHT

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
        for i in range(6):
            self.blobHandler.new_blob()
        self.food = []


        grid = self.query_one("#grid", Container)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                grid.mount(Static(EMPTY, id=f"cell_{x}_{y}"))

        self.blob_list = self.blobHandler.get_blobs()
        self.render_grid()

        self.set_interval(0.5, self.update_sim)

    def render_grid(self) -> None:
        blob_positions = {b.pos: [BLOB_DIRS[b.facing], b.color] for b in self.blob_list}
        food_set = set(self.food)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                pos = (x, y)
                cell = self.query_one(f"#cell_{x}_{y}", Static)

                if pos in blob_positions:
                    symbol, color = blob_positions[pos]
                    text = Text(symbol)
                    text.stylize(color)
                    cell.update(text)
                elif pos in food_set:
                    cell.update(FOOD)
                else:
                    cell.update(EMPTY)
                    cell.remove_class(*cell.classes)

    def update_sim(self):
        self.blob_list = self.blobHandler.get_blobs()
        self.blobHandler.update()
        self.render_grid()

    def quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = NeuroEvolve()
    app.run()