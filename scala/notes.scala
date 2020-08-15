
//REPL reevaluate print loop

/*
fgrando@thinkx:~$ scala
Welcome to Scala 2.11.12 (OpenJDK 64-Bit Server VM, Java 11.0.8).
Type in expressions for evaluation. Or try :help.

scala> 10 + 3
res0: Int = 13

scala> "result " + res0
res1: String = result 13

scala> "val cannot change"
res2: String = val cannot change

scala> "var can change"
res3: String = var can change

scala> val = 123
<console>:1: error: illegal start of simple pattern
val = 123
    ^

scala> val a=123
a: Int = 123

scala> var b=321
b: Int = 321

scala> a=12
<console>:12: error: reassignment to val
       a=12
        ^

scala> b=12
b: Int = 12

// importing libs
scala> import scala.math._
import scala.math._

scala> abs(-80)
res8: Int = 80


scala> (random * (11-1)+1).toInt
res16: Int = 2

scala> toDegrees(123)
res17: Double = 7047.380880109125



*/

// types

Byte by     // -128 to 128
Boolean bo  // true or false
Char ch     // uint16 65535
Short sh    // Int16 -32768 to 32767
Int   in    // -2147483648 to 2147483647
Long  ln    // -9223372036854775808 to 92233720368547758077
Float fl    // -3.4028235E38 to 3.4028235E38
Double dl   // -1.7976931348623157E308 to 1.7976931348623157E307

val lgprime = BigInt("123465789")
val lgprime = BigDecimal("123.465789")