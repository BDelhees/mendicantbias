# Data Science and Toolkits

### Milestone 3

#### 1.


#### 2.


#### 3.

To find what datatypes of each object in bitcoin.csv we run (pandas is required):

```sh
python3 df.dtypes
```

Output is as follows:

| Variable | Type in Python| Type in PostgresSQL (precision, scale)|
| --- | --- | --- |
| Timestamp |   int64  | NUMERIC(10)
| Open |  float64   | NUMERIC
| High |  float64   | NUMERIC
| Low |   float64  | NUMERIC
| Close |   float64  | NUMERIC
| Volume_(BTC)  |float64     | NUMERIC
| Volume_(Currency) |   float64  | NUMERIC
| Weighted_Price  |   float64  | NUMERIC
| date |  datetime64   | ISO 8601
| dtype |  object   |

PostgresSQL does not support any 64-byte integers or floats (int64, float64) according to https://www.postgresql.org/docs/12/datatype-numeric.html#DATATYPE-INT. This leaves us with the following option to structure our database. Change the float64 and int64 to NUMERIC. However, this will slow down calculations comapred to PostgresSQL int-types. Nevertheless, the calculations are more precise and recommended for monetary amounts. This trade-off between precision and time needs to be observed in real-time. The int64 could technically be converted to int8 in python (with the numpy package) but this cuts down the possible range of values from -128 to 127 (see https://numpy.org/doc/stable/user/basics.types.html). This would be possible for the "Volume_(BTC)" variable but not for the others. We therefore stick to NUMERIC for now. Also, we want to keep the option of a larger precision (total amount of numbers for a given observation) and scale (numbers after the decimal points). This is mostly for the float-variables which would give us closer predictions of our Rnn-Model. The timestamp variable is an int with a precision of 10, so int8 is not an option without major transformations. We refrain from using the direct money type since there could arise problems when classifying BTC as a currency.

To find the largest and lowest numbers for each variable, we run:

```sh
python3 df.max()
python3 df.min()
```
This reveals:

| Variable | Max| Min|
| --- | --- | ---|
| Timestamp | 1421421480    | 1417411980
| Open |  398   | 109.87
| High |  398   | 109.94
| Low |   398  | 109.87
| Close |   398  | 109.94
| Volume_(BTC)  |5.2     | 0.01
| Volume_(Currency) |   1965.6  | 1.0994
| Weighted_Price  |   398  | 109.94
| date |  2015-01-16   | 2014-12-01
| dtype |  object   | object
