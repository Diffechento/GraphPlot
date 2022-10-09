import matplotlib.pyplot as plt
from collections import namedtuple
import click


class FileRead:
    def __init__(self, filename):
        self.filename = filename

    def read_axis_names(self):
        with open(self.filename, "r") as f:
            axis_names = f.readline()
        f.close()
        names = namedtuple("names", "x y z")
        return names(axis_names.strip().split(" ")[0], axis_names.strip().split(" ")[1],
                     axis_names.strip().split(" ")[2])

    def read_xyz(self):
        x = []
        y = []
        z = []
        with open(self.filename, "r") as f:
            for line in f.readlines():
                try:
                    x.append(float(line.strip().split(" ")[0]))
                    y.append(float(line.strip().split(" ")[1]))
                    z.append(float(line.strip().split(" ")[2]))
                except ValueError:
                    pass
        f.close()
        coords = namedtuple("coords", "x y z")
        return coords(x, y, z)


@click.command()
@click.option('--path', help='Path to file with samples')
def main(path):
    data_file = FileRead(path)
    fig = plt.figure(figsize=(7, 4))
    ax_3d = fig.add_subplot(projection='3d')
    axis_names = data_file.read_axis_names()
    coords = data_file.read_xyz()
    ax_3d.plot(coords.z, coords.y, coords.x)
    ax_3d.set_xlabel(axis_names.x)
    ax_3d.set_ylabel(axis_names.y)
    ax_3d.set_zlabel(axis_names.z)
    plt.show()


if __name__ == '__main__':
    main()
