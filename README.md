# Extended Euclidean Algorithm
An algorithm to efficiently calculate the GCD of two numbers.

## Usage
Any one of the following, depending on the OS this program is running on.
```bash
python3 <file_name> a b
py <file_name> a b
py3 <file_name> a b
```

## Input constraints
Since `int` type in python3 does not have a fixed length, the input size constraint depends on the hardware. For example, the acceptable range on a 64-bit machine is -2<sup>63</sup> ≤ `num` ≤ 2<sup>63</sup>-1. Note that (a,b)≠(0,0), as this GCD is not defined.

## Note
Although the program accepts negative numbers as input, the program takes the absolute values before doing any operations. The GCD should remain unchanged, but the linear combination formula will be changed.

## Examples
Numbers that are coprime
```bash
>> python3 euclidean_algo.py 1092384 9803
       a     b    q     r
 1092384  9803  111  4251
    9803  4251    2  1301
    4251  1301    3   348
    1301   348    3   257
     348   257    1    91
     257    91    2    75
      91    75    1    16
      75    16    4    11
      16    11    1     5
      11     5    2     1
       5     1    5     0

>> The GCD of 1092384 and 9803 is: 1
>> 1 = 204035 x 9803 + -1831 x 1092384
```
Numbers that are not coprime
```bash
>> python3 euclidean_algo.py 1092384 184 
       a    b     q    r
 1092384  184  5936  160
     184  160     1   24
     160   24     6   16
      24   16     1    8
      16    8     2    0

>> The GCD of 1092384 and 184 is: 8
>> 8 = 47495 x 184 + -8 x 1092384
```
One of the numbers is 0
```bash
>> python3 euclidean_algo.py 8937 0     
>> The GCD of 0 and 8937 is: 8937
>> By definition
```
One of the numbers is negative
```bash
>> python3 euclidean_algo.py -12378 972 
     a    b   q    r
 12378  972  12  714
   972  714   1  258
   714  258   2  198
   258  198   1   60
   198   60   3   18
    60   18   3    6
    18    6   3    0

>> The GCD of 12378 and 972 is: 6
>> 6 = 624 x 972 + -49 x 12378
```
Both numbers are negative
```bash
>> python3 euclidean_algo.py -1956 -198236
      a     b    q    r
 198236  1956  101  680
   1956   680    2  596
    680   596    1   84
    596    84    7    8
     84     8   10    4
      8     4    2    0

>> The GCD of 198236 and 1956 is: 4
>> 4 = 233 x 198236 + -23614 x 1956
```
