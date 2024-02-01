# Solving a Sudoku

The following image shows a challenging Sudoku puzzle.

<table border="2">
  <tr>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #aaaaaa;color: black"> 9 </td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> 1 </td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> 2 </td>
  </tr>
  <tr>
    <td style="background: #dddddd;color: black"> 7 </td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #aaaaaa;color: black"> 3 </td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> 6 </td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> 2 </td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #aaaaaa;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
    <td style="background: #dddddd;color: black"> 3 </td>
    <td style="background: #dddddd;color: black"> &nbsp;&nbsp;</td>
  </tr>
  <tr>
    <td style="background: #aaaaaa;color: black"> 9 </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #dddddd;color: black">  </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> 8 </td>
    <td style="background: #aaaaaa;color: black"> 7 </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
  </tr>
  <tr>
    <td style="background: #aaaaaa;color: black"> 3 </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> 1 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> 9 </td>
  </tr>
  <tr>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> 6 </td>
    <td style="background: #dddddd;color: black"> 5 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> 1 </td>
  </tr>
  <tr>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> 1 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #dddddd;color: black"> 4 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
  </tr>
  <tr>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> 4 </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> 9 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> 6 </td>
  </tr>
  <tr>
    <td style="background: #dddddd;color: black"> 8 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> 3 </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> </td>
    <td style="background: #aaaaaa;color: black"> 6 </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
    <td style="background: #dddddd;color: black"> </td>
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