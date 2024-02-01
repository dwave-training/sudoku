# Solving a Sudoku

The following image shows a challenging Sudoku puzzle.

<table border="2">
  <tr>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td style="border: none"></td>
    <td> 9 </td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td style="border: none"></td>
    <td> 1 </td>
    <td> &nbsp;&nbsp;</td>
    <td> 2 </td>
  </tr>
  <tr>
    <td> 7 </td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td style="border: none"></td>
    <td> 3 </td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td style="border: none"></td>
    <td> 6 </td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td> 2 </td>
    <td style="border: none"></td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td> &nbsp;&nbsp;</td>
    <td style="border: none"></td>
    <td> &nbsp;&nbsp;</td>
    <td> 3 </td>
    <td> &nbsp;&nbsp;</td>
  </tr>
  <tr></tr>
  <tr></tr>
  <tr>
    <td> 9 </td>
    <td> </td>
    <td> </td>
    <td style="border: none"></td>
    <td>  </td>
    <td> </td>
    <td> 8 </td>
    <td style="border: none"></td>
    <td> 7 </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td> 3 </td>
    <td> </td>
    <td> </td>
    <td style="border: none"></td>
    <td> </td>
    <td> 1 </td>
    <td> </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> 9 </td>
  </tr>
  <tr>
    <td> </td>
    <td> </td>
    <td> 6 </td>
    <td style="border: none"></td>
    <td> 5 </td>
    <td> </td>
    <td> </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> 1 </td>
  </tr>
  <tr></tr>
  <tr></tr>
  <tr>
    <td> </td>
    <td> 1 </td>
    <td> </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> </td>
    <td style="border: none"></td>
    <td> 4 </td>
    <td> </td>
    <td> </td>
  </tr>
  <tr>
    <td> </td>
    <td> </td>
    <td> 4 </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> 9 </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> 6 </td>
  </tr>
  <tr>
    <td> 8 </td>
    <td> </td>
    <td> 3 </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> 6 </td>
    <td style="border: none"></td>
    <td> </td>
    <td> </td>
    <td> </td>
  </tr>
</table>

A sudoku puzzle solution must satisfy the following rules.

 1. Each column has the numbers 1-9 exactly once.
 2. Each row has the numbers 1-9 exactly once.
 3. If we divide the grid into 9 subsquares by grouping rows/columns (0-2), (3-5), and (6-8), each subsquare has the numbers 1-9 exactly once.

## The Exercise

Use the framework code provided to solve the Sudoku puzzle provided. The rules provided describe three different types of constraints.

### Provided Code

The code provided includes an initial definition of variables to be used. Binary variables have been defined as `x[i][j][k]`, where `i` indicates the row index, `j` indicates the column index, and `k` indicates a digit from 1-9. Using this description, we define `x[i][j][k] == 1` if the entry in row `i`, column `j` equals digit `k`.