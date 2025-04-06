# tth
`tth` is a python library for creating truth tables in Microsoft Word documents.

It allows python syntax for creating columns of truth table.

For example, to create a truth table for the following:
$$
A \overline{B} C
$$

You just have to do the following:

```python
from tth import Column, make_table_document

# note the third argument to `Column`
# constructor for `B` and `C`. It is required
# in all the columns that are not first column.

A = Column(pos=1, total_inputs=3)
B = Column(pos=2, total_inputs=3, first_col=A)
C = Column(pos=3, total_inputs=3, first_col=A)

# Now, simply write the operation as:
A & ~B & C

# Call the document creator function like this
make_table_document(first_col=A, filename_to_save="file_name.docx")
```

Note that providing kw arguments is not required, they are there to help you understand the API.
