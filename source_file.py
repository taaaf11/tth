from __future__ import annotations

from collections.abc import Sequence



class Column:
    def __init__(self, pos: int, total_inputs: int, latex: str | None = None, values: Sequence[int] | None = None, first_col: Column | None= None):
        self.pos = pos
        if not (pos == -1 and total_inputs == -1):
            if pos > total_inputs or pos == 0:
                raise Exception("Invalid column position")

            construction_values = []
            
            # there are two states: 0 and 1
            # For the first column in a total of three columns
            # there are 8 / 2 = 4 number of each state
            # this means that first column has four zero's and four one's
            number_of_each_state = 2 ** (total_inputs - pos)
            total_entries = 2 ** total_inputs
            
            while len(construction_values) < total_entries:
                for _ in range(number_of_each_state):
                    construction_values.append(0)
                
                for _ in range(number_of_each_state):
                    construction_values.append(1)

            self.__values = tuple(construction_values)
        else:
            self.__values = tuple(values)
        self.__nrows = len(self.__values)

        # self.__latex = ord('A') - 1 + pos
        
        self.latex = latex or chr(ord('A') - 1 + pos)
        
        self.first_col = first_col
        if first_col is not None:
            first_col.table.append([self.latex, *self.values])
        else:
            self.table = [[self.latex, *self.values]]
            self.first_col = self
        
        # if pos != -1:
            # self.table.append()
            # self.table = []
            # self.table.append([self.latex, *self.values])
        # else:
            # self.table.append([latex, values])

        # table.append([self.latex, *self.values])
        # self.table = table
        

    @property
    def values(self) -> tuple[int, ...]:
        return self.__values

    @property
    def nrows(self) -> int:
        return self.__nrows
    
    def __neg__(self) -> Column:
        new_values = tuple(map(lambda x: int(not x), self.values, strict=True))
        new_col_latex = fr"\overline{self.latex}"
        new_col = Column(-1, -1, latex=new_col_latex, values=new_values, first_col=self.first_col)
        return new_col
    
    def __and__(self, other: Column) -> Column:
        new_values = tuple(map(lambda vals: int(vals[0] and vals[1]), zip(self.values, other.values, strict=True)))
        new_col_latex = f"{self.latex} \\cdot {other.latex}"
        new_col = Column(-1, -1, latex=new_col_latex, values=new_values, first_col=self.first_col)
        return new_col
    
    def __or__(self, other: Column) -> Column:
        new_values = tuple(map(lambda x, y: int(x or y), zip(self.values, other.values)))
        new_col_latex = fr"{self.latex}{other.latex}"
        new_col = Column(-1, -1, latex=new_col_latex, values=new_values, first_col=self.first_col)
        return new_col
    
    
def make_table(first_col: Column, )
        

A = Column(1, 2)
B = Column(2, 2, first_col=A)
# print((A.__and__(B) ))
anded = A & B
# print(((A & B)).table)
print(A.table)

# print(A.table)


# print(A.values)
# print(B.values)