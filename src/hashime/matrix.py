from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Matrix(ABC, Generic[T]):
    """
    2D matrix.
    """

    def __init__(
        self, width: int, height: int, fill: T, digest: bytes | None = None
    ) -> None:
        """
        Initializes a matrix.

        Args:
            width: Matrix width.
            height : Matrix height.
            fill: Default matrix value.
        """
        self._matrix = [[fill for _ in range(width)] for _ in range(height)]
        self._x = width // 2
        self._y = height // 2
        if digest is not None:
            self.update(digest)

    def update(self, data: bytes) -> None:
        for byte in data:
            self._process_byte(byte)

    @abstractmethod
    def _process_byte(self, byte: int) -> None:
        pass

    def __getitem__(self, key: tuple[int, int]) -> T:
        x, y = key
        return self._matrix[y][x]

    def __setitem__(self, key: tuple[int, int], value: T) -> None:
        x, y = key
        self._matrix[y][x] = value

    @property
    def width(self) -> int:
        """
        Matrix width.
        """
        if not self._matrix:
            return 0
        return len(self._matrix[0])

    @property
    def height(self) -> int:
        """
        Matrix height.
        """
        return len(self._matrix)

    def overlay(
        self,
        other: 'Matrix[T]',
        x_off: int,
        y_off: int,
        ignore: T | None = None,
    ) -> 'Matrix[T]':
        """
        Overlays a matrix over this one.

        Args:
            other: Matrix to overlay.
            x_off: X-axis offset.
            y_off: Y-axis offset.
            ignore: Value to ignore while overlaying.

        Returns:
            Self.
        """
        for y, row in enumerate(other._matrix):
            for x, val in enumerate(row):
                if val == ignore:
                    continue
                new_y = y + y_off
                new_x = x + x_off
                if 0 <= new_y < self.height and 0 <= new_x < self.width:
                    self[new_x, new_y] = val
        return self

    def reverse(self) -> 'Matrix[T]':
        """
        Horizontally mirrors the matrix.

        Returns:
            Self.
        """
        for row in self._matrix:
            row.reverse()
        return self

    @classmethod
    def from_matrix(cls, matrix: list[list[T]]) -> 'Matrix[T]':
        """
        Initializes a matrix from a pre-made matrix.

        Args:
            matrix: Pre-made matrix.

        Returns:
            A matrix.
        """
        new = cls.__new__(cls)
        new._matrix = matrix
        return new

    @abstractmethod
    def to_art(self) -> str:
        """
        Generates randomart.

        Returns:
            Randomart.
        """
        pass
