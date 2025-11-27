from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from BlobHandler import BlobHandler
from constants import BLOB_DIRS, FOOD, EMPTY, WIDTH, HEIGHT
#🡸🡺🡹🡻🡽🡾🡼🡿


"""  """

class NeuroEvolve(App):

    CSS = """
        Static {
            width: 100%;
            height: 100%;
            content-align: center middle;
        }

        #grid {
            layout: grid;
            grid-size: 10 10;
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
        self.blobHandler.new_blob()
        self.food = []

        self.blob_list = self.blobHandler.get_blobs()
        self.render_grid()

        self.set_interval(0.5, self.update_sim)

    def render_grid(self) -> None:
        grid = self.query_one("#grid", Container)
        grid.remove_children()

        for y in range(HEIGHT):
            for x in range(WIDTH):
                for b in self.blob_list:
                    if (x, y) == b.pos:
                        grid.mount(Static(BLOB_DIRS[b.facing]))
                        break
                    elif (x, y) in self.food:
                        grid.mount(Static(FOOD))
                        break
                    else:
                        grid.mount(Static(EMPTY))


    def update_sim(self):
        self.blob_list = self.blobHandler.get_blobs()
        self.blobHandler.update()
        self.render_grid()

    def quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = NeuroEvolve()
    app.run()