    # Fountain Code: Efficient Pytho   n Implementation of LT Codes

Th   is project is the implementation    in Python of the iterative enco   ding and iterative decoding algo   rithms of the [LT Codes](https:/   /en.wikipedia.org/wiki/LT_codes)   ,
an error correction code based    on the principles of [Fountain    	Codes](https://en.wikipedia.org/   
wiki/Fountain_code) by Michael L   uby.
I have written a whole arti   cle on LT Codes and this snippet    that you can find here : [franp   apers.com](https://franpapers.co   m/en/algorithmic/2018-introducti   on-to-fountain-codes-lt-codes-wi   th-python/)

The encoder and dec   oder are optimized to handle big    transfers for files between 1MB    to 1GB at high speed.

### Inst   allation

This implementation re   quires at least python 3.x.
Some    packages are not built-in. To i   nstall them with `pip` you can d   o:

```
$ pip install -r require   ments.txt
```

## Usage

An exam   ple describing how to use the im   plementation is in `lt_codes.py`   , and you can use it to encode/d   ecode a file on the fly (creates    a file copy):
```
$ python lt_c    odes.py filename [-h] [-r REDUND   !ANCY] [--systematic] [--verbose]   " [--x86]
```

As an example, her   #e is a basic test to ensure the    $integrity of the final file:
```   %
$ echo "Hello!" > test.txt
$ py   &thon lt_codes.py test.txt --syst   'ematic
```
A new file test-copy.   (txt should be created with the s   )ame content.

### Content

* `co   *re.py` contains the Symbol class   +, constants and functions that a   ,re used in both encoding and dec   -oding.
* `distributions.py` cont   .ains the two functions that gene   /rate degrees based on the ideal    0soliton and robust soliton distr   1ibutions
* `encoder.py` contains   2 the encoding algorithm
* `decod   3er.py` contains the decoding alg   4orithm
* `md5_checker.sh` calls    5`lt_codes.py` and then compare t   6he integrity of the original fil   7e with the newly created file. T   8he integrity check is made with    9`md5sum`, add the ".exe" if you    :work on Window. Replace it by `m   ;d5 -r` if you work on Mac, or ru   <n `brew install md5sha1sum`.

##   = Benchmarks
The time consumed by   > the encoding and decoding proce   ?ss is completely related to the    @size of the file to encode and t   Ahe wanted redundancy.
I have mad   Be some measure on an Intel i5 @    C2.30GHz with a 1.5 redundancy :
   D
<table>
<thead>
<tr>
<td rowspa   En="2"><strong>Size (MB)</strong>   F</td>
<td rowspan="2"><strong>Bl   Gocks</strong></td>
<td rowspan="   H2"><strong>Symbols</strong></td>   I
<td colspan="2"><strong>Encodin   Jg</strong></td>
<td colspan="2">   K<strong>Decoding</strong></td>
<   L/tr>
<tr>
<td><strong>Time (s)</   Mstrong></td>
<td><strong>Speed (   NMB/s)</strong></td>
<td><strong>   OTime (s)</strong></td>
<td><stro   Png>Speed (MB/s)</strong></td>
</   Qtr>
</thead>
<tbody>
<tr>
<td>1<   R/td>
<td>16</td>
<td>24</td>
<td   S>0.00</td>
<td>-</td>
<td>0.00</   Ttd>
<td>-</td>
</tr>
<tr>
<td>10   U0</td>
<td>1600</td>
<td>2400</t   Vd>
<td>0.21</td>
<td>476.1</td>
   W<td>0.31</td>
<td>322.5</td>
</t   Xr>
<tr>
<td>1200</td>
<td>19200<   Y/td>
<td>28800</td>
<td>3.86</td   Z>
<td>310.8</td>
<td>39.82</td>
   [<td>30.1</td>
</tr>
<tr>
<td>200   \0</td>
<td>32000</td>
<td>48000<   ]/td>
<td>6.44</td>
<td>310.5</td   ^>
<td>104.10</td>
<td>19.2</td>
   _</tr>
<tr>
<td>3600</td>
<td>576   `00</td>
<td>86400</td>
<td>23.14   a</td>
<td>155.5</td>
<td>426.36<   b/td>
<td>8.4</td>
</tr>
</tbody>   c
</table>

<img src="https://fra   dnpapers.com/wp-content/uploads/2   e018/06/word-image-18.png" width=   f500 />

Note: `PACKET_SIZE` is s   get to 65536 for theses tests. Lo   hwering it will result in lower s   ipeeds but it might be necessary    jto send small files in many chun   kks.


## References

> M.Luby, "   lLT Codes", The 43rd Annual IEEE    mSymposium on Foundations of Comp   nuter Science, 2002.

## License
   o
MIT License
Copyright (c) 2018    pFrançois Andrieux

Permission i   qs hereby granted, free of charge   r, to any person obtaining a copy   s of this software and associated   t documentation files (the "Softw   uare"), to deal in the Software w   vithout restriction, including wi   wthout limitation the rights to u   xse, copy, modify, merge, publish   y, distribute, sublicense, and/or   z sell copies of the Software, an   {d to permit persons to whom the    |Software is furnished to do so,    }subject to the following conditi   ~ons:

The above copyright notice    and this permission notice shal   �l be included in all copies or s   �ubstantial portions of the Softw   �are.

THE SOFTWARE IS PROVIDED "   �AS IS", WITHOUT WARRANTY OF ANY    �KIND, EXPRESS OR IMPLIED, INCLUD   �ING BUT NOT LIMITED TO THE WARRA   �NTIES OF MERCHANTABILITY, FITNES   �S FOR A PARTICULAR PURPOSE AND N   �ONINFRINGEMENT. IN NO EVENT SHAL   �L THE AUTHORS OR COPYRIGHT HOLDE   �RS BE LIABLE FOR ANY CLAIM, DAMA   �GES OR OTHER LIABILITY, WHETHER    �IN AN ACTION OF CONTRACT, TORT O   �R OTHERWISE, ARISING FROM, OUT O   �F OR IN CONNECTION WITH THE SOFT   �WARE OR THE USE OR OTHER DEALING   �S IN THE SOFTWARE.

