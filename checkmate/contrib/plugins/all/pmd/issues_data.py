# -*- coding: utf-8 -*-


issues_data = {

    "CallSuperLast": {
        "title": "super should be called at the end of the method",
        "display_name": "CallSuperLast",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Super should be called at the end of the method\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/android.html#CallSuperLast\n\n      \npublic class DummyActivity extends Activity {\n\tpublic void onPause() {\n\t\tfoo();\n\t\t// missing call to super.onPause()\n\t}\n}\n\n    "
    },
    "TooManyFields": {
        "title": "Too many fields",
        "display_name": "TooManyFields",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Classes that have too many fields can become unwieldy and could be redesigned to have fewer fields, possibly through grouping related fields in new objects. For example, a class with individual city/state/zip fields could park them within a single Address field.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#TooManyFields\n\n   \nCREATE OR REPLACE PACKAGE pkg_too_many_fields AS\n    C_CHAR_A CONSTANT CHAR(1 CHAR) := 'A';\n    C_CHAR_B CONSTANT CHAR(1 CHAR) := 'B';\n    ...\n    C_CHAR_Z CONSTANT CHAR(1 CHAR) := 'Z';\nEND pkg_too_many_fields;\n\n   \n      "
    },
    "UnnecessaryCaseChange": {
        "title": "Using equalsIgnoreCase() is cleaner than using toUpperCase/toLowerCase().equals().",
        "display_name": "UnnecessaryCaseChange",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Using equalsIgnoreCase() is faster than using toUpperCase/toLowerCase().equals()\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#UnnecessaryCaseChange\n\n       \nboolean answer1 = buz.toUpperCase().equals(\"baz\");\t \t\t// should be buz.equalsIgnoreCase(\"baz\")\n    \nboolean answer2 = buz.toUpperCase().equalsIgnoreCase(\"baz\");\t // another unnecessary toUpperCase()\n \n       "
    },
    "JUnitTestContainsTooManyAsserts": {
        "title": "JUnit tests should not contain more than ${maximumAsserts} assert(s).",
        "display_name": "JUnitTestContainsTooManyAsserts",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "JUnit tests should not contain too many asserts. Many asserts are indicative of a complex test, for which it is harder to verify correctness. Consider breaking the test scenario into multiple, shorter test scenarios. Customize the maximum number of assertions used by this Rule to suit your needs.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#JUnitTestContainsTooManyAsserts\n\n\npublic class MyTestCase extends TestCase {\n\t// Ok\n\tpublic void testMyCaseWithOneAssert() {\n\t\tboolean myVar = false;\t\t\n\t\tassertFalse(\"should be false\", myVar);\n\t}\n\n\t// Bad, too many asserts (assuming max=1)\n\tpublic void testMyCaseWithMoreAsserts() {\n\t\tboolean myVar = false;\t\t\n\t\tassertFalse(\"myVar should be false\", myVar);\n\t\tassertEquals(\"should equals false\", false, myVar);\n\t}\n}\n\n\t\t"
    },
    "UseAssertTrueInsteadOfAssertEquals": {
        "title": "Use assertTrue(x)/assertFalse(x) instead of assertEquals(true, x)/assertEquals(false, x)   or assertEquals(Boolean.TRUE, x)/assertEquals(Boolean.FALSE, x).",
        "display_name": "UseAssertTrueInsteadOfAssertEquals",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When asserting a value is the same as a literal or Boxed boolean, use assertTrue/assertFalse, instead of assertEquals.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#UseAssertTrueInsteadOfAssertEquals\n\n\npublic class MyTestCase extends TestCase {\n\tpublic void testMyCase() {\n\t\tboolean myVar = true;\n\t\t// Ok\n\t\tassertTrue(\"myVar is true\", myVar);\n\t\t// Bad\n\t\tassertEquals(\"myVar is true\", true, myVar);\n\t\t// Bad\n\t\tassertEquals(\"myVar is false\", false, myVar);\n\t\t// Bad\n\t\tassertEquals(\"myVar is true\", Boolean.TRUE, myVar);\n\t\t// Bad\n\t\tassertEquals(\"myVar is false\", Boolean.FALSE, myVar);\n\t}\n}\n\n\t\t"
    },
    "ShortClassName": {
        "title": "Avoid short class names like {0}",
        "display_name": "ShortClassName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Short Classnames with fewer than e.g. five characters are not recommended.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#ShortClassName\n\n    \npublic class Foo {\n}\n    \n        "
    },
    "SuspiciousOctalEscape": {
        "title": "Suspicious decimal characters following octal escape in string literal",
        "display_name": "SuspiciousOctalEscape",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A suspicious octal escape sequence was found inside a String literal. The Java language specification (section 3.10.6) says an octal escape sequence inside a literal String shall consist of a backslash followed by: OctalDigit | OctalDigit OctalDigit | ZeroToThree OctalDigit OctalDigit Any octal escape sequence followed by non-octal digits can be confusing, e.g. \"\\038\" is interpreted as the octal escape sequence \"\\03\" followed by the literal character \"8\".\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#SuspiciousOctalEscape\n\n\npublic void foo() {\n  // interpreted as octal 12, followed by character '8'\n  System.out.println(\"suspicious: \\128\");\n}\n\n      "
    },
    "EmptyFinallyBlock": {
        "title": "Avoid empty finally blocks",
        "display_name": "EmptyFinallyBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty finally blocks serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyFinallyBlock\n\n  \npublic class Foo {\n public void bar() {\n  try {\n    int x=2;\n   } finally {\n    // empty!\n   }\n }\n}\n \n      "
    },
    "ApexBadCrypto": {
        "title": "Apex classes should use random IV/key",
        "display_name": "ApexBadCrypto",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The rule makes sure you are using randomly generated IVs and keys for `Crypto` calls. Hard-wiring these values greatly compromises the security of encrypted data.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexBadCrypto\n\n            \npublic without sharing class Foo {\n    Blob hardCodedIV = Blob.valueOf('Hardcoded IV 123');\n    Blob hardCodedKey = Blob.valueOf('0000000000000000');\n    Blob data = Blob.valueOf('Data to be encrypted');\n    Blob encrypted = Crypto.encrypt('AES128', hardCodedKey, hardCodedIV, data);\n}\n    \n        "
    },
    "StringBufferInstantiationWithChar": {
        "title": "Do not instantiate a StringBuffer or StringBuilder with a char",
        "display_name": "StringBufferInstantiationWithChar",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Individual character values provided as initialization arguments will be converted into integers. This can lead to internal buffer sizes that are larger than expected. Some examples: new StringBuffer() // 16 new StringBuffer(6) // 6 new StringBuffer(\"hello world\") // 11 + 16 = 27 new StringBuffer('A') // chr(A) = 65 new StringBuffer(\"A\") // 1 + 16 = 17 new StringBuilder() // 16 new StringBuilder(6) // 6 new StringBuilder(\"hello world\") // 11 + 16 = 27 new StringBuilder('C') // chr(C) = 67 new StringBuilder(\"A\") // 1 + 16 = 17\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#StringBufferInstantiationWithChar\n\n\n\t// misleading instantiation, these buffers\n\t// are actually sized to 99 characters long\nStringBuffer  sb1 = new StringBuffer('c');   \nStringBuilder sb2 = new StringBuilder('c');\n  \n// in these forms, just single characters are allocated\nStringBuffer  sb3 = new StringBuffer(\"c\");\nStringBuilder sb4 = new StringBuilder(\"c\");\n\n    "
    },
    "JUnitStaticSuite": {
        "title": "You have a suite() method that is not both public and static, so JUnit won't call it to get your TestSuite.  Is that what you wanted to do?",
        "display_name": "JUnitStaticSuite",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The suite() method in a JUnit test needs to be both public and static.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#JUnitStaticSuite\n\n  \nimport junit.framework.*;\n\npublic class Foo extends TestCase {\n   public void suite() {}         // oops, should be static\n   private static void suite() {} // oops, should be public\n}\n  \n      "
    },
    "AvoidCatchingNPE": {
        "title": "Avoid catching NullPointerException; consider removing the cause of the NPE.",
        "display_name": "AvoidCatchingNPE",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Code should never throw NullPointerExceptions under normal circumstances. A catch block may hide the original error, causing other, more subtle problems later on.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidCatchingNPE\n  \npublic class Foo {\n  void bar() {\n    try {\n      // do something\n      }  catch (NullPointerException npe) {\n    }\n  }\n}\n\n    "
    },
    "AvoidFieldNameMatchingTypeName": {
        "title": "It is somewhat confusing to have a field name matching the declaring class name",
        "display_name": "AvoidFieldNameMatchingTypeName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "It is somewhat confusing to have a field name matching the declaring class name. This probably means that type and/or field names should be chosen more carefully.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#AvoidFieldNameMatchingTypeName\n\n\npublic class Foo extends Bar {\n\tint foo;\t// There is probably a better name that can be used\n}\n\n      "
    },
    "UnnecessaryConversionTemporary": {
        "title": "Avoid unnecessary temporaries when converting primitives to Strings",
        "display_name": "UnnecessaryConversionTemporary",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid the use temporary objects when converting primitives to Strings. Use the static conversion methods on the wrapper classes instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UnnecessaryConversionTemporary\n\n  \npublic String convert(int x) {\n\tString foo = new Integer(x).toString();\t// this wastes an object\n\t\n\treturn Integer.toString(x);\t\t\t\t// preferred approach\n}\n \n      "
    },
    "MissingSerialVersionUID": {
        "title": "Classes implementing Serializable should set a serialVersionUID",
        "display_name": "MissingSerialVersionUID",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Serializable classes should provide a serialVersionUID field.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/javabeans.html#MissingSerialVersionUID\n\n\npublic class Foo implements java.io.Serializable {\n String name;\n // Define serialization id to avoid serialization related bugs\n // i.e., public static final long serialVersionUID = 4328743;\n}\n\n\n          "
    },
    "CallSuperFirst": {
        "title": "super should be called at the start of the method",
        "display_name": "CallSuperFirst",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Super should be called at the start of the method\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/android.html#CallSuperFirst\n\npublic class DummyActivity extends Activity {\n\tpublic void onCreate(Bundle bundle) {\n     // missing call to super.onCreate(bundle)\n\t\tfoo();\n\t}\n}\n\n    "
    },
    "UnusedImports": {
        "title": "Avoid unused imports such as ''{0}''",
        "display_name": "UnusedImports",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid unused import statements. This rule will find unused on demand imports, i.e. import com.foo.*.\r\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/typeresolution.html#UnusedImports\r\n\r\n\r\nimport java.io.*;\t// not referenced or required\r\n\r\npublic class Foo {}\r\n\r\n    "
    },
    "UseArrayListInsteadOfVector": {
        "title": "Use ArrayList instead of Vector",
        "display_name": "UseArrayListInsteadOfVector",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "ArrayList is a much better Collection implementation than Vector if thread-safe operation is not required.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#UseArrayListInsteadOfVector\n\n\npublic class SimpleTest extends TestCase {\n\tpublic void testX() {\n\t\tCollection c1 = new Vector();\t\t\n\t\tCollection c2 = new ArrayList();\t// achieves the same with much better performance\n\t}\n}\n\n          "
    },
    "UnusedMacroParameter": {
        "title": "Avoid unused macro parameters such as ''{0}''",
        "display_name": "UnusedMacroParameter",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid unused macro parameters. They should be deleted.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#UnusedMacroParameter\n"
    },
    "BooleanInstantiation": {
        "title": "Avoid instantiating Boolean objects; reference Boolean.TRUE or Boolean.FALSE or call Boolean.valueOf() instead.",
        "display_name": "BooleanInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid instantiating Boolean objects; you can reference Boolean.TRUE, Boolean.FALSE, or call Boolean.valueOf() instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#BooleanInstantiation\n\n   \nBoolean bar = new Boolean(\"true\");\t\t// unnecessary creation, just reference Boolean.TRUE;\nBoolean buz = Boolean.valueOf(false);\t// ...., just reference Boolean.FALSE;\n   \n   "
    },
    "UnnecessaryWrapperObjectCreation": {
        "title": "Unnecessary wrapper object creation",
        "display_name": "UnnecessaryWrapperObjectCreation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Most wrapper classes provide static conversion methods that avoid the need to create intermediate objects just to create the primitive forms. Using these avoids the cost of creating objects that also need to be garbage-collected later.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#UnnecessaryWrapperObjectCreation\n\n\npublic int convert(String s) {\n  int i, i2;\n\n  i = Integer.valueOf(s).intValue(); // this wastes an object\n  i = Integer.parseInt(s); \t\t\t // this is better\n\n  i2 = Integer.valueOf(i).intValue(); // this wastes an object\n  i2 = i; // this is better\n\n  String s3 = Integer.valueOf(i2).toString(); // this wastes an object\n  s3 = Integer.toString(i2); \t\t// this is better\n\n  return i2;\n}\n\n          "
    },
    "ExcessiveObjectLength": {
        "title": "Avoid really long Oracle object specifications and bodies ({0} lines found).",
        "display_name": "ExcessiveObjectLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Excessive object line lengths are usually indications that the object may be burdened with excessive responsibilities that could be provided by other objects. In breaking these methods apart the code becomes more managable and ripe for reuse.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#ExcessiveObjectLength\n\n\nCREATE OR REPLACE\nPACKAGE BODY Foo AS\n\tPROCEDURE bar1 IS BEGIN\n    -- 1000 lines of code\n\tEND bar1;\n\tPROCEDURE bar2 IS BEGIN\n    -- 1000 lines of code\n\tEND bar2;\n    PROCEDURE bar3 IS BEGIN\n    -- 1000 lines of code\n\tEND bar3;\n\t\n\t\n    PROCEDURE barN IS BEGIN\n    -- 1000 lines of code\n\tEND barn;\nEND;\n\n   "
    },
    "EqualsNull": {
        "title": "Avoid using equals() to compare against null",
        "display_name": "EqualsNull",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Tests for null should not use the equals() method. The '==' operator should be used instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#EqualsNull\n\n       \nString x = \"foo\";\n\nif (x.equals(null)) { // bad form\n   \tdoSomething();\n\t}\n\nif (x == null) { \t// preferred\n   \tdoSomething();\n\t}\n    \n        "
    },
    "EmptyIfStmt": {
        "title": "Avoid empty if statements",
        "display_name": "EmptyIfStmt",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty if statements should be deleted.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#EmptyIfStmt\n"
    },
    "ClassCastExceptionWithToArray": {
        "title": "This usage of the Collection.toArray() method will throw a ClassCastException.",
        "display_name": "ClassCastExceptionWithToArray",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When deriving an array of a specific class from your Collection, one should provide an array of the same class as the parameter of the toArray() method. Doing otherwise you will will result in a ClassCastException.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#ClassCastExceptionWithToArray\n\n\nCollection c = new ArrayList();\nInteger obj = new Integer(1);\nc.add(obj);\n\n    // this would trigger the rule (and throw a ClassCastException if executed)\nInteger[] a = (Integer [])c.toArray();\n\n   // this is fine and will not trigger the rule\nInteger[] b = (Integer [])c.toArray(new Integer[c.size()]);\n\n  "
    },
    "DontCallThreadRun": {
        "title": "Don't call Thread.run() explicitly, use Thread.start()",
        "display_name": "DontCallThreadRun",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Explicitly calling Thread.run() method will execute in the caller's thread of control. Instead, call Thread.start() for the intended behavior.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#DontCallThreadRun\n\n\nThread t = new Thread();\nt.run();            // use t.start() instead\nnew Thread().run(); // same violation\n\n      "
    },
    "TestClassWithoutTestCases": {
        "title": "This class name ends with 'Test' but contains no test cases",
        "display_name": "TestClassWithoutTestCases",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Test classes end with the suffix Test. Having a non-test class with that name is not a good practice, since most people will assume it is a test case. Test classes have test methods named testXXX.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#TestClassWithoutTestCases\n\n\n//Consider changing the name of the class if it is not a test\n//Consider adding test methods if it is a test\npublic class CarTest {\n   public static void main(String[] args) {\n    // do something\n   }\n   // code\n}\n\n      "
    },
    "CheckSkipResult": {
        "title": "Check the value returned by the skip() method of an InputStream to see if the requested number of bytes has been skipped.",
        "display_name": "CheckSkipResult",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The skip() method may skip a smaller number of bytes than requested. Check the returned value to find out if it was the case or not.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#CheckSkipResult\n\n        \npublic class Foo {\n\n   private FileInputStream _s = new FileInputStream(\"file\");\n\n   public void skip(int n) throws IOException {\n      _s.skip(n); // You are not sure that exactly n bytes are skipped\n   }\n\n   public void skipExactly(int n) throws IOException {\n      while (n != 0) {\n         long skipped = _s.skip(n);\n         if (skipped == 0)\n            throw new EOFException();\n         n -= skipped;\n      }\n   }\n        \n        "
    },
    "CompareObjectsWithEquals": {
        "title": "Use equals() to compare object references.",
        "display_name": "CompareObjectsWithEquals",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use equals() to compare object references; avoid comparing them with ==.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#CompareObjectsWithEquals\n\n\nclass Foo {\n  boolean bar(String a, String b) {\n    return a == b;\n  }\n}\n\n\n  "
    },
    "NPathComplexity": {
        "title": "The method {0}() has an NPath complexity of {1}",
        "display_name": "NPathComplexity",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The NPath complexity of a method is the number of acyclic execution paths through that method. A threshold of 200 is generally considered the point where measures should be taken to reduce complexity and increase readability.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#NPathComplexity\n\n \nCREATE OR REPLACE\nPROCEDURE bar AS BEGIN\t-- this is something more complex than it needs to be,\n\tif (y) THEN\t-- it should be broken down into smaller methods or functions\n\t\tfor j IN 0 .. j-1 LOOP\n\t\t\tif (j > r) THEN\n\t\t\t\tdoSomething;\n\t\t\t\twhile (f < 5 ) LOOP\n\t\t\t\t\tanotherThing;\n\t\t\t\t\tf := f - 27;\n\t\t\t\t\tEND LOOP;\n\t\t\telse\n\t\t\t\t\ttryThis();\n\t\t\tEND IF;\n\t\tEND LOOP;\n\tEND IF;\n\tif ( r - n > 45) THEN\n\t\twhile (doMagic) LOOP\n\t\t\tfindRabbits;\n\t\tEND LOOP;\n\tEND IF;\n\tBEGIN\n\t\tdoSomethingDangerous();\n\tEXCEPTION WHEN FooException THEN\n\t\tmakeAmends;\n\t\tBEGIN\n\t\t\tdontDoItAgain;\n\t\tEXCEPTION\n\t\tWHEN OTHERS THEN\n\t\t\t\tlog_problem;\n\t\tEND;\n\tEND;\nEND;\n\n \n    "
    },
    "ClassNamingConventions": {
        "title": "Class names should begin with an uppercase character",
        "display_name": "ClassNamingConventions",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Class names should always begin with an upper case character.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#ClassNamingConventions\n\n\npublic class Foo {}\n\n      "
    },
    "LongInstantiation": {
        "title": "Avoid instantiating Long objects.Call Long.valueOf() instead",
        "display_name": "LongInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calling new Long() causes memory allocation that can be avoided by the static Long.valueOf(). It makes use of an internal cache that recycles earlier instances making it more memory efficient.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#LongInstantiation\n\n\npublic class Foo {\n\tprivate Long i = new Long(0); // change to Long i = Long.valueOf(0);\n}\n\n    "
    },
    "BigIntegerInstantiation": {
        "title": "Don't create instances of already existing BigInteger and BigDecimal (ZERO, ONE, TEN)",
        "display_name": "BigIntegerInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Don't create instances of already existing BigInteger (BigInteger.ZERO, BigInteger.ONE) and for Java 1.5 onwards, BigInteger.TEN and BigDecimal (BigDecimal.ZERO, BigDecimal.ONE, BigDecimal.TEN)\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#BigIntegerInstantiation\n\n\nBigInteger bi = new BigInteger(1);\t\t// reference BigInteger.ONE instead\nBigInteger bi2 = new BigInteger(\"0\");\t// reference BigInteger.ZERO instead\nBigInteger bi3 = new BigInteger(0.0);\t// reference BigInteger.ZERO instead\nBigInteger bi4;\nbi4 = new BigInteger(0);\t\t\t\t// reference BigInteger.ZERO instead\n\n  "
    },
    "UnnecessaryModifier": {
        "title": "Avoid modifiers which are implied by the context",
        "display_name": "UnnecessaryModifier",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Fields in interfaces and annotations are automatically `public static final`, and methods are `public abstract`. Classes, interfaces or annotations nested in an interface or annotation are automatically `public static` (all nested interfaces and annotations are automatically static). Nested enums are automatically `static`. For historical reasons, modifiers which are implied by the context are accepted by the compiler, but are superfluous.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UnnecessaryModifier\n\n \n public @interface Annotation {\n  public abstract void bar(); \t\t// both abstract and public are ignored by the compiler\n  public static final int X = 0; \t// public, static, and final all ignored\n  public static class Bar {} \t\t// public, static ignored\n  public static interface Baz {} \t// ditto\n}\npublic interface Foo {\n  public abstract void bar(); \t\t// both abstract and public are ignored by the compiler\n  public static final int X = 0; \t// public, static, and final all ignored\n  public static class Bar {} \t\t// public, static ignored\n  public static interface Baz {} \t// ditto\n}\npublic class Bar {\n  public static interface Baz {} // static ignored\n  public static enum FoorBar { // static ignored\n    FOO;\n  }\n}\n \n     "
    },
    "BrokenNullCheck": {
        "title": "Method call on object which may be null",
        "display_name": "BrokenNullCheck",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The null check is broken since it will throw a NullPointerException itself. It is likely that you used || instead of && or vice versa.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#BrokenNullCheck\n\n\npublic String bar(String string) {\n  // should be &&\n\tif (string!=null || !string.equals(\"\"))\n\t\treturn string;\n  // should be ||\n\tif (string==null && string.equals(\"\"))\n\t\treturn string;\n}\n        \n        "
    },
    "OnlyOneReturn": {
        "title": "A method should have only one exit point, and that should be the last statement in the method",
        "display_name": "OnlyOneReturn",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A method should have only one exit point, and that should be the last statement in the method.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#OnlyOneReturn\n\n \npublic class OneReturnOnly1 {\n  public void foo(int x) {\n    if (x > 0) {\n      return \"hey\";   // first exit\n    }\n    return \"hi\";\t// second exit\n  }\n}\n \n     "
    },
    "AbstractNaming": {
        "title": "Abstract classes should be named 'AbstractXXX'",
        "display_name": "AbstractNaming",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Abstract classes should be named 'AbstractXXX'.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#AbstractNaming\n\n\npublic abstract class Foo { // should be AbstractFoo\n}\n\n       "
    },
    "UnusedLocalVariable": {
        "title": "Avoid unused local variables such as ''{0}''.",
        "display_name": "UnusedLocalVariable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects when a local variable is declared and/or assigned, but not used.\r\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unusedcode.html#UnusedLocalVariable\r\n\r\n\r\npublic class Foo {\r\n\tpublic void doSomething() {\r\n\t\tint i = 5; // Unused\r\n\t}\r\n}\r\n\r\n    "
    },
    "UnusedPrivateMethod": {
        "title": "Avoid unused private methods such as ''{0}''.",
        "display_name": "UnusedPrivateMethod",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Unused Private Method detects when a private method is declared but is unused.\r\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unusedcode.html#UnusedPrivateMethod\r\n\r\n\r\npublic class Something {\r\n\tprivate void foo() {} // unused\r\n}\r\n\r\n    "
    },
    "UnnecessaryReturn": {
        "title": "Avoid unnecessary return statements",
        "display_name": "UnnecessaryReturn",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid the use of unnecessary return statements.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UnnecessaryReturn\n\n\t\t\npublic class Foo {\n  public void bar() {\n    int x = 42;\n    return;\n  }\n}\n\t\t\n      "
    },
    "AvoidInstanceofChecksInCatchClause": {
        "title": "An instanceof check is being performed on the caught exception.  Create a separate catch clause for this exception type.",
        "display_name": "AvoidInstanceofChecksInCatchClause",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Each caught exception type should be handled in its own catch clause.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AvoidInstanceofChecksInCatchClause\n\n\ntry { // Avoid this\n // do something\n} catch (Exception ee) {\n if (ee instanceof IOException) {\n  cleanup();\n }\n}\ntry {  // Prefer this:\n // do something\n} catch (IOException ee) {\n cleanup();\n}\n\n      "
    },
    "VfUnescapeEl": {
        "title": "Avoid unescaped user controlled content in EL",
        "display_name": "VfUnescapeEl",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid unescaped user controlled content in EL as it results in XSS.\nhttps://pmd.github.io/pmd-5.8.1/pmd-visualforce/rules/vf/security.html#VfUnescapeElRule\n\n\t\t\t \n<apex:outputText value=\"Potential XSS is {! here }\" escape=\"false\" />\n\t\t\t \n\t\t"
    },
    "AvoidUsingHardCodedIP": {
        "title": "Do not hard code the IP address ${variableName}",
        "display_name": "AvoidUsingHardCodedIP",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Application with hard-coded IP addresses can become impossible to deploy in some cases. Externalizing IP adresses is preferable.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#AvoidUsingHardCodedIP\n\n\t    \npublic class Foo {\n\tprivate String ip = \"127.0.0.1\"; \t// not recommended\n}\n\t    \n\t    "
    },
    "AvoidThrowingNullPointerException": {
        "title": "Avoid throwing null pointer exceptions.",
        "display_name": "AvoidThrowingNullPointerException",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid throwing NullPointerExceptions. These are confusing because most people will assume that the virtual machine threw it. Consider using an IllegalArgumentException instead; this will be clearly seen as a programmer-initiated exception.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidThrowingNullPointerException\n\n        \npublic class Foo {\n  void bar() {\n    throw new NullPointerException();\n  }\n}\n  \n      "
    },
    "EmptySwitchStatements": {
        "title": "Avoid empty switch statements",
        "display_name": "EmptySwitchStatements",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty switch statements serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptySwitchStatements\n\n  \npublic void bar() {\n\tint x = 2;\n\tswitch (x) {\n\t// once there was code here\n\t// but it's been commented out or something\n\t}\n}\n\n      "
    },
    "ExtendsObject": {
        "title": "No need to explicitly extend Object.",
        "display_name": "ExtendsObject",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "No need to explicitly extend Object.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#ExtendsObject\n\n    \npublic class Foo extends Object { \t// not required\n}\n    \n    "
    },
    "ImportFromSamePackage": {
        "title": "No need to import a type that lives in the same package",
        "display_name": "ImportFromSamePackage",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "There is no need to import a type that lives in the same package.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/imports.html#ImportFromSamePackage\n\n \n package foo;\n \n import foo.Buz; // no need for this\n import foo.*; // or this\n \n public class Bar{}\n \n     "
    },
    "UseCorrectExceptionLogging": {
        "title": "Use the correct logging statement for logging exceptions",
        "display_name": "UseCorrectExceptionLogging",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "To make sure the full stacktrace is printed out, use the logging statement with two arguments: a String and a Throwable.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-jakarta-commons.html#UseCorrectExceptionLogging\n\npublic class Main {\n   private static final Log _LOG = LogFactory.getLog( Main.class );\n   void bar() {\n     try {\n     } catch( Exception e ) {\n      _LOG.error( e ); //Wrong!\n     } catch( OtherException oe ) {\n      _LOG.error( oe.getMessage(), oe ); //Correct\n     }\n   }\n}\n"
    },
    "ConstantsInInterface": {
        "title": "Avoid constants in interfaces. Interfaces define types, constants are implementation details better placed in classes or enums. See Effective Java, item 19.",
        "display_name": "ConstantsInInterface",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid constants in interfaces. Interfaces should define types, constants are implementation details better placed in classes or enums. See Effective Java, item 19.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#ConstantsInInterface\n\n\npublic interface ConstantInterface {\n    public static final int CONST1 = 1; // violation, no fields allowed in interface!\n    static final int CONST2 = 1; // violation, no fields allowed in interface!\n    final int CONST3 = 1; // violation, no fields allowed in interface!\n    int CONST4 = 1; // violation, no fields allowed in interface!\n}\n\n// with ignoreIfHasMethods = false\npublic interface AnotherConstantInterface {\n    public static final int CONST1 = 1; // violation, no fields allowed in interface!\n\n    int anyMethod();\n}\n\n// with ignoreIfHasMethods = true\npublic interface YetAnotherConstantInterface {\n    public static final int CONST1 = 1; // no violation\n\n    int anyMethod();\n}\n \n        "
    },
    "SuspiciousConstantFieldName": {
        "title": "The field name indicates a constant but its modifiers do not",
        "display_name": "SuspiciousConstantFieldName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Field names using all uppercase characters - Sun's Java naming conventions indicating constants - should be declared as final.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#SuspiciousConstantFieldName\n\n    \npublic class Foo {\n // this is bad, since someone could accidentally\n // do PI = 2.71828; which is actually e\n // final double PI = 3.16; is ok\n  double PI = 3.16;\n}\n    \n       "
    },
    "AvoidDecimalLiteralsInBigDecimalConstructor": {
        "title": "Avoid creating BigDecimal with a decimal (float/double) literal. Use a String literal",
        "display_name": "AvoidDecimalLiteralsInBigDecimalConstructor",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "One might assume that the result of \"new BigDecimal(0.1)\" is exactly equal to 0.1, but it is actually equal to .1000000000000000055511151231257827021181583404541015625. This is because 0.1 cannot be represented exactly as a double (or as a binary fraction of any finite length). Thus, the long value that is being passed in to the constructor is not exactly equal to 0.1, appearances notwithstanding. The (String) constructor, on the other hand, is perfectly predictable: 'new BigDecimal(\"0.1\")' is exactly equal to 0.1, as one would expect. Therefore, it is generally recommended that the (String) constructor be used in preference to this one.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#AvoidDecimalLiteralsInBigDecimalConstructor\n\n\nBigDecimal bd = new BigDecimal(1.123);\t\t// loss of precision, this would trigger the rule\n\nBigDecimal bd = new BigDecimal(\"1.123\");   \t// preferred approach\n\nBigDecimal bd = new BigDecimal(12);     \t// preferred approach, ok for integer values\n\n  "
    },
    "GuardLogStatementJavaUtil": {
        "title": "There is log block not surrounded by if",
        "display_name": "GuardLogStatementJavaUtil",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Whenever using a log level, one should check if the loglevel is actually enabled, or otherwise skip the associate String creation and manipulation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-java.html#GuardLogStatementJavaUtil\n\n \n \t// Add this for performance\n\tif (log.isLoggable(Level.FINE)) { ...\n \t    log.fine(\"log something\" + \" and \" + \"concat strings\");\n\n     "
    },
    "AvoidPrefixingMethodParameters": {
        "title": "Avoid prefixing parameters by in, out or inOut. Uses Javadoc to document this behavior.",
        "display_name": "AvoidPrefixingMethodParameters",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Prefixing parameters by 'in' or 'out' pollutes the name of the parameters and reduces code readability. To indicate whether or not a parameter will be modify in a method, its better to document method behavior with Javadoc.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidPrefixingMethodParameters\n\n// Not really clear\npublic class Foo {\n  public void bar(\n      int inLeftOperand,\n      Result outRightOperand) {\n      outRightOperand.setValue(inLeftOperand * outRightOperand.getValue());\n  }\n}\n        "
    },
    "AvoidReassigningParameters": {
        "title": "Avoid reassigning macro parameters such as ''{0}''",
        "display_name": "AvoidReassigningParameters",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Reassigning values to incoming parameters is not recommended. Use temporary local variables instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#AvoidReassigningParameters\n"
    },
    "UnconditionalIfStatement": {
        "title": "Do not use 'if' statements that are always true or always false",
        "display_name": "UnconditionalIfStatement",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Do not use \"if\" statements whose conditionals are always true or always false.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#UnconditionalIfStatement\n\n  \npublic class Foo {\n\tpublic void close() {\n\t\tif (true) {\t\t// fixed conditional, not recommended\n\t\t\t// ...\n\t\t}\n\t}\n}\n\n      "
    },
    "CloseResource": {
        "title": "Ensure that resources like this {0} object are closed after use",
        "display_name": "CloseResource",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Ensure that resources (like Connection, Statement, and ResultSet objects) are always closed after use.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#CloseResource\n\n\npublic class Bar {\n  public void foo() {\n    Connection c = pool.getConnection();\n    try {\n      // do stuff\n    } catch (SQLException ex) {\n     // handle exception\n    } finally {\n      // oops, should close the connection using 'close'!\n      // c.close();\n    }\n  }\n}\n\n    "
    },
    "DoNotThrowExceptionInFinally": {
        "title": "A throw statement in a finally block makes the control flow hard to understand.",
        "display_name": "DoNotThrowExceptionInFinally",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Throwing exceptions within a 'finally' block is confusing since they may mask other exceptions or code defects. Note: This is a PMD implementation of the Lint4j rule \"A throw in a finally block\"\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#DoNotThrowExceptionInFinally\n\n    \t\t\npublic class Foo {\n\tpublic void bar() {\n\t\ttry {\n\t\t\t// Here do some stuff\n\t\t} catch( Exception e) {\n\t\t\t// Handling the issue\n\t\t} finally {\n\t\t\t// is this really a good idea ?\n\t\t\tthrow new Exception();\n\t\t}\n\t}\n}\n\t    \t\n    \t"
    },
    "EmptyStatementNotInLoop": {
        "title": "An empty statement (semicolon) not part of a loop",
        "display_name": "EmptyStatementNotInLoop",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "An empty statement (or a semicolon by itself) that is not used as the sole body of a 'for' or 'while' loop is probably a bug. It could also be a double semicolon, which has no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyStatementNotInLoop\n\n\npublic void doit() {\n      // this is probably not what you meant to do\n      ;\n      // the extra semicolon here this is not necessary\n      System.out.println(\"look at the extra semicolon\");;\n}\n\n       "
    },
    "AvoidFieldNameMatchingMethodName": {
        "title": "Field {0} has the same name as a method",
        "display_name": "AvoidFieldNameMatchingMethodName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "It can be confusing to have a field name with the same name as a method. While this is permitted, having information (field) and actions (method) is not clear naming. Developers versed in Smalltalk often prefer this approach as the methods denote accessor methods.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#AvoidFieldNameMatchingMethodName\n\n\npublic class Foo {\n\tObject bar;\n\t// bar is data or an action or both?\n\tvoid bar() {\n\t}\n}\n\n      "
    },
    "ConsecutiveAppendsShouldReuse": {
        "title": "StringBuffer (or StringBuilder).append is called consecutively without reusing the target variable.",
        "display_name": "ConsecutiveAppendsShouldReuse",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Consecutive calls to StringBuffer/StringBuilder .append should be chained, reusing the target object. This can improve the performance by producing a smaller bytecode, reducing overhead and improving inlining. A complete analysis can be found [here](https://github.com/pmd/pmd/issues/202#issuecomment-274349067)\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#ConsecutiveAppendsShouldReuse\n\n\nString foo = \" \";\n\nStringBuffer buf = new StringBuffer();\nbuf.append(\"Hello\"); // poor\nbuf.append(foo);\nbuf.append(\"World\");\n\nStringBuffer buf = new StringBuffer();\nbuf.append(\"Hello\").append(foo).append(\"World\"); // good\n\n    "
    },
    "UseNotifyAllInsteadOfNotify": {
        "title": "Call Thread.notifyAll() rather than Thread.notify()",
        "display_name": "UseNotifyAllInsteadOfNotify",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Thread.notify() awakens a thread monitoring the object. If more than one thread is monitoring, then only one is chosen. The thread chosen is arbitrary; thus its usually safer to call notifyAll() instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UseNotifyAllInsteadOfNotify\n\n\n  void bar() {\n    x.notify();\n    // If many threads are monitoring x, only one (and you won't know which) will be notified.\n    // use instead:\n    x.notifyAll();\n  }\n\n      "
    },
    "AvoidTrailingComma": {
        "title": "Avoid trailing commas in object or array literals",
        "display_name": "AvoidTrailingComma",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule helps improve code portability due to differences in browser treatment of trailing commas in object or array literals.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#AvoidTrailingComma\n\n\nfunction(arg) {\n    var obj1 = { a : 1 }; // Ok\n    var arr1 = [ 1, 2 ]; // Ok\n\n    var obj2 = { a : 1, }; // Syntax error in some browsers!\n    var arr2 = [ 1, 2, ]; // Length 2 or 3 depending on the browser!\n}\n\n        "
    },
    "GenericsNaming": {
        "title": "Generics names should be a one letter long and upper case.",
        "display_name": "GenericsNaming",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Names for references to generic values should be limited to a single uppercase letter.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#GenericsNaming\n\n            \npublic interface GenericDao<E extends BaseModel, K extends Serializable> extends BaseDao {\n   // This is ok...\n}\n\npublic interface GenericDao<E extends BaseModel, K extends Serializable> {\n   // Also this\n}\n\npublic interface GenericDao<e extends BaseModel, K extends Serializable> {\n   // 'e' should be an 'E'\n}\n\npublic interface GenericDao<EF extends BaseModel, K extends Serializable> {\n   // 'EF' is not ok.\n}\n     "
    },
    "UseStringBufferLength": {
        "title": "This is an inefficient use of StringBuffer.toString; call StringBuffer.length instead.",
        "display_name": "UseStringBufferLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use StringBuffer.length() to determine StringBuffer length rather than using StringBuffer.toString().equals(\"\") or StringBuffer.toString().length() == ...\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#UseStringBufferLength\n\n  \nStringBuffer sb = new StringBuffer();\n    \nif (sb.toString().equals(\"\")) {}\t    // inefficient \n    \nif (sb.length() == 0) {}\t    \t\t// preferred\n  \n      "
    },
    "EmptySynchronizedBlock": {
        "title": "Avoid empty synchronized blocks",
        "display_name": "EmptySynchronizedBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty synchronized blocks serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptySynchronizedBlock\n\n\npublic class Foo {\n public void bar() {\n  synchronized (this) {\n   // empty!\n  }\n }\n}\n\n      "
    },
    "MoreThanOneLogger": {
        "title": "Class contains more than one logger.",
        "display_name": "MoreThanOneLogger",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Normally only one logger is used in each class.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-java.html#MoreThanOneLogger\n\n \npublic class Foo {\n    Logger log = Logger.getLogger(Foo.class.getName());\n    // It is very rare to see two loggers on a class, normally\n    // log information is multiplexed by levels\n    Logger log2= Logger.getLogger(Foo.class.getName());\n}\n\n     "
    },
    "ReplaceEnumerationWithIterator": {
        "title": "Consider replacing this Enumeration with the newer java.util.Iterator",
        "display_name": "ReplaceEnumerationWithIterator",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Consider replacing Enumeration usages with the newer java.util.Iterator\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#ReplaceEnumerationWithIterator\n\n    \npublic class Foo implements Enumeration {\n    private int x = 42;\n    public boolean hasMoreElements() {\n        return true;\n    }\n    public Object nextElement() {\n        return String.valueOf(i++);\n    }\n}\n    \n      "
    },
    "BadComparison": {
        "title": "Avoid equality comparisons with Double.NaN",
        "display_name": "BadComparison",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid equality comparisons with Double.NaN. Due to the implicit lack of representation precision when comparing floating point numbers these are likely to cause logic errors.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#BadComparison\n\n  \nboolean x = (y == Double.NaN);\n  \n      "
    },
    "AccessorClassGeneration": {
        "title": "Avoid instantiation through private constructors from outside of the constructor's class.",
        "display_name": "AccessorClassGeneration",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Instantiation by way of private constructors from outside of the constructor's class often causes the generation of an accessor. A factory method, or non-privatization of the constructor can eliminate this situation. The generated class file is actually an interface. It gives the accessing class the ability to invoke a new hidden package scope constructor that takes the interface as a supplementary parameter. This turns a private constructor effectively into one with package scope, and is challenging to discern.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AccessorClassGeneration\n\n  \npublic class Outer {\n void method(){\n  Inner ic = new Inner();//Causes generation of accessor class\n }\n public class Inner {\n  private Inner(){}\n }\n}\n  \n      "
    },
    "SuspiciousHashcodeMethodName": {
        "title": "The method name and return type are suspiciously close to hashCode()",
        "display_name": "SuspiciousHashcodeMethodName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The method name and return type are suspiciously close to hashCode(), which may denote an intention to override the hashCode() method.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#SuspiciousHashcodeMethodName\n\n    \npublic class Foo {\n\tpublic int hashcode() {\t// oops, this probably was supposed to be 'hashCode'\n\t\n\t}\n}\n    \n       "
    },
    "UseBaseWithParseInt": {
        "title": "Always provide a base when using parseInt() functions",
        "display_name": "UseBaseWithParseInt",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "TODO\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#UseBaseWithParseInt\n\nparseInt(\"10\",base);\n  "
    },
    "AvoidStringBufferField": {
        "title": "StringBuffers can grow quite a lot, and so may become a source of memory leak (if the owning class has a long life time).",
        "display_name": "AvoidStringBufferField",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "StringBuffers/StringBuilders can grow considerably, and so may become a source of memory leaks if held within objects with long lifetimes.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#AvoidStringBufferField\n\n\npublic class Foo {\n\tprivate StringBuffer buffer;\t// potential memory leak as an instance variable;\n}\n\n\t\t"
    },
    "DataflowAnomalyAnalysis": {
        "title": "Found ''{0}''-anomaly for variable ''{1}'' (lines ''{2}''-''{3}'').",
        "display_name": "DataflowAnomalyAnalysis",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The dataflow analysis tracks local definitions, undefinitions and references to variables on different paths on the data flow. From those informations there can be found various problems. 1. UR - Anomaly: There is a reference to a variable that was not defined before. This is a bug and leads to an error. 2. DU - Anomaly: A recently defined variable is undefined. These anomalies may appear in normal source text. 3. DD - Anomaly: A recently defined variable is redefined. This is ominous but don't have to be a bug.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#DataflowAnomalyAnalysis\n\n\npublic void foo() {\n  int buz = 5;\n  buz = 6; // redefinition of buz -> dd-anomaly\n  foo(buz);\n  buz = 2;\n} // buz is undefined when leaving scope -> du-anomaly\n\n          "
    },
    "ApexUnitTestClassShouldHaveAsserts": {
        "title": "Apex unit tests should System.assert() or assertEquals() or assertNotEquals()",
        "display_name": "ApexUnitTestClassShouldHaveAsserts",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Apex unit tests should include at least one assertion. This makes the tests more robust, and using assert with messages provide the developer a clearer idea of what the test does.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/apexunit.html#ApexUnitTestClassShouldHaveAsserts\n\n            \n@isTest\npublic class Foo {\n   public static testMethod void testSomething() {\n      Account a = null;\n   // This is better than having a NullPointerException\n   // System.assertNotEquals(a, null, 'account not found');\n   a.toString();\n   }\n}\n    \n        "
    },
    "NoInlineStyles": {
        "title": "Avoid inline styles",
        "display_name": "NoInlineStyles",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid inline styles. Use css classes instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#NoInlineStyles\n"
    },
    "UseCollectionIsEmpty": {
        "title": "Substitute calls to size() == 0 (or size() != 0, size() > 0, size() < 1) with calls to isEmpty()",
        "display_name": "UseCollectionIsEmpty",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The isEmpty() method on java.util.Collection is provided to determine if a collection has any elements. Comparing the value of size() to 0 does not convey intent as well as the isEmpty() method.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UseCollectionIsEmpty\n\n    \npublic class Foo {\n\tvoid good() {\n       \tList foo = getList();\n\t\tif (foo.isEmpty()) {\n\t\t\t// blah\n\t\t}\n   \t}\n\n    void bad() {\n   \t    List foo = getList();\n\t\t\tif (foo.size() == 0) {\n\t\t\t\t// blah\n\t\t\t}\n    \t}\n}\n    \n      "
    },
    "ByteInstantiation": {
        "title": "Avoid instantiating Byte objects. Call Byte.valueOf() instead",
        "display_name": "ByteInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calling new Byte() causes memory allocation that can be avoided by the static Byte.valueOf(). It makes use of an internal cache that recycles earlier instances making it more memory efficient.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#ByteInstantiation\n\n\npublic class Foo {\n\tprivate Byte i = new Byte(0); // change to Byte i =\tByte.valueOf(0);\n}\n\n     "
    },
    "ProjectVersionAsDependencyVersion": {
        "title": "Do not use project's version to express a dependency's version.",
        "display_name": "ProjectVersionAsDependencyVersion",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Using that expression in dependency declarations seems like a shortcut, but it can go wrong. By far the most common problem is the use of ${project.version} in a BOM or parent POM.\nhttps://pmd.github.io/pmd-5.8.1/pmd-xml/rules/pom/basic.html#ProjectVersionAsDependencyVersion\n\n \n<project...>\n  ...\n  <dependency>\n    ...\n    <version>${project.dependency}</version>\n  </dependency>\n</project>\n \n     "
    },
    "AvoidPrintStackTrace": {
        "title": "Avoid printStackTrace(); use a logger call instead.",
        "display_name": "AvoidPrintStackTrace",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid printStackTrace(); use a logger call instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-java.html#AvoidPrintStackTrace\n\n\nclass Foo {\n  void bar() {\n    try {\n     // do something\n    } catch (Exception e) {\n     e.printStackTrace();\n     }\n   }\n}\n\n           "
    },
    "UnnecessaryConstructor": {
        "title": "Avoid unnecessary constructors - the compiler will generate these for you",
        "display_name": "UnnecessaryConstructor",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule detects when a constructor is not necessary; i.e., when there is only one constructor, its public, has an empty body, and takes no arguments.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#UnnecessaryConstructor\n\n  \npublic class Foo {\n  public Foo() {}\n}\n  \n      "
    },
    "DontImportSun": {
        "title": "Avoid importing anything from the 'sun.*' packages",
        "display_name": "DontImportSun",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid importing anything from the 'sun.*' packages. These packages are not portable and are likely to change.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#DontImportSun\n\n\nimport sun.misc.foo;\npublic class Foo {}\n\n       "
    },
    "AvoidDuplicateLiterals": {
        "title": "The String literal {0} appears {1} times in this file; the first occurrence is on line {2}",
        "display_name": "AvoidDuplicateLiterals",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Code containing duplicate String literals can usually be improved by declaring the String as a constant field.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#AvoidDuplicateLiterals\n\n\nprivate void bar() {\n     buz(\"Howdy\");\n     buz(\"Howdy\");\n     buz(\"Howdy\");\n     buz(\"Howdy\");\n }\n private void buz(String x) {}\n\n    "
    },
    "SwitchDensity": {
        "title": "A high ratio of statements to labels in a switch statement.  Consider refactoring.",
        "display_name": "SwitchDensity",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A high ratio of statements to labels in a switch statement implies that the switch statement is overloaded. Consider moving the statements into new methods or creating subclasses based on the switch variable.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SwitchDensity\n\n \npublic class Foo {\n  public void bar(int x) {\n    switch (x) {\n      case 1: {\n        // lots of statements\n        break;\n      } case 2: {\n        // lots of statements\n        break;\n      }\n    }\n  }\n}\n \n      "
    },
    "TomKytesDespair": {
        "title": "WHEN OTHERS THEN NULL - when you do this, Tom Kyte cries",
        "display_name": "TomKytesDespair",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "\"WHEN OTHERS THEN NULL\" hides all errors - (Re)RAISE an exception or call RAISE_APPLICATION_ERROR\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/TomKytesDespair.html#TomKytesDespair\n\n\nCREATE OR REPLACE PACKAGE BODY update_planned_hrs\nIS\n \nPROCEDURE set_new_planned (p_emp_id IN NUMBER, p_project_id IN NUMBER, p_hours IN NUMBER)\nIS\nBEGIN\n   UPDATE employee_on_activity ea\n   SET ea.ea_planned_hours = p_hours\n   WHERE\n            ea.ea_emp_id = p_emp_id            \n            AND ea.ea_proj_id = p_project_id;\n \nEXCEPTION\n          WHEN NO_DATA_FOUND THEN\n           RAISE_APPLICATION_ERROR (-20100, 'No such employee or project');\n \nEND set_new_planned;\n \nFUNCTION existing_planned (p_emp_id IN NUMBER, p_project_id IN NUMBER) RETURN NUMBER\n \nIS\n \nexisting_hours NUMBER(4);\n \nBEGIN\n   SELECT ea.ea_planned_hours INTO existing_hours \n   FROM employee_on_activity ea\n   WHERE\n            ea.ea_emp_id = p_emp_id     \n            AND ea.ea_proj_id = p_project_id; \n \n   RETURN (existing_hours);\n \n   EXCEPTION\n          WHEN OTHERS THEN NULL;\n \n   END existing_planned;\n \nEND update_planned_hrs;\n/\n\n  "
    },
    "SimplifyBooleanReturns": {
        "title": "Avoid unnecessary if..then..else statements when returning booleans",
        "display_name": "SimplifyBooleanReturns",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid unnecessary if-then-else statements when returning a boolean. The result of the conditional test can be returned instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SimplifyBooleanReturns\n\n\npublic boolean isBarEqualTo(int x) {\n\n\tif (bar == x) {\t\t // this bit of code...\n\t\treturn true;\n\t} else {\n\t\treturn false;\n    }\n}\n\npublic boolean isBarEqualTo(int x) {\n\n   \treturn bar == x;\t// can be replaced with this\n}\n\n    "
    },
    "CommentRequired": {
        "title": "Comment is required",
        "display_name": "CommentRequired",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Denotes whether comments are required (or unwanted) for specific language elements.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/comments.html#CommentRequired\n\n\n/**\n* \n*\n* @author George Bush\n*/\n\n    "
    },
    "ConsecutiveLiteralAppends": {
        "title": "StringBuffer (or StringBuilder).append is called {0} consecutive times with literal Strings. Use a single append with a single combined String.",
        "display_name": "ConsecutiveLiteralAppends",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Consecutively calling StringBuffer/StringBuilder.append with String literals\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#ConsecutiveLiteralAppends\n\n\nStringBuffer buf = new StringBuffer();\nbuf.append(\"Hello\").append(\" \").append(\"World\"); // poor\nbuf.append(\"Hello World\");        \t\t\t\t // good\n\n    "
    },
    "StringInstantiation": {
        "title": "Avoid instantiating String objects; this is usually unnecessary.",
        "display_name": "StringInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid instantiating String objects; this is usually unnecessary since they are immutable and can be safely shared.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#StringInstantiation\n\n\nprivate String bar = new String(\"bar\"); // just do a String bar = \"bar\";\n\n    "
    },
    "PackageCase": {
        "title": "Package name contains upper case characters",
        "display_name": "PackageCase",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects when a package definition contains uppercase characters.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#PackageCase\n\n    \npackage com.MyCompany;  // should be lowercase name\n\npublic class SomeClass {\n}\n    \n        "
    },
    "CheckResultSet": {
        "title": "Always check the return of one of the navigation method (next,previous,first,last) of a ResultSet.",
        "display_name": "CheckResultSet",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Always check the return values of navigation methods (next, previous, first, last) of a ResultSet. If the value return is 'false', it should be handled properly.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#CheckResultSet\n\n            \nStatement stat = conn.createStatement();\nResultSet rst = stat.executeQuery(\"SELECT name FROM person\");\nrst.next(); \t// what if it returns false? bad form\nString firstName = rst.getString(1);\n\nStatement stat = conn.createStatement();\nResultSet rst = stat.executeQuery(\"SELECT name FROM person\");\nif (rst.next()) {\t// result is properly examined and used\n    String firstName = rst.getString(1);\n\t} else  {\n\t\t// handle missing data\n}\n            \n        "
    },
    "ApexCSRF": {
        "title": "Avoid making DML operations in Apex class constructor/init method",
        "display_name": "ApexCSRF",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Check to avoid making DML operations in Apex class constructor/init method. This prevents modification of the database just by accessing a page.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexCSRF\n\n            \npublic class Foo {\n    public init() {\n        insert data;\n    }\n\n    public Foo() {\n        insert data;\n    }\n}\n    \n        "
    },
    "ReturnFromFinallyBlock": {
        "title": "Avoid returning from a finally block",
        "display_name": "ReturnFromFinallyBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid returning from a finally block, this can discard exceptions.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#ReturnFromFinallyBlock\n\n  \npublic class Bar {\n\tpublic String foo() {\n\t\ttry {\n\t\t\tthrow new Exception( \"My Exception\" );\n\t\t} catch (Exception e) {\n\t\t\tthrow e;\n\t\t} finally {\n\t\t\treturn \"A. O. K.\"; // return not recommended here\n\t\t}\n\t}\n}\n\n      "
    },
    "UseAssertEqualsInsteadOfAssertTrue": {
        "title": "Use assertEquals(x, y) instead of assertTrue(x.equals(y))",
        "display_name": "UseAssertEqualsInsteadOfAssertTrue",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule detects JUnit assertions in object equality. These assertions should be made by more specific methods, like assertEquals.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#UseAssertEqualsInsteadOfAssertTrue\n\n\npublic class FooTest extends TestCase {\n\tvoid testCode() {\n\t\tObject a, b;\n\t\tassertTrue(a.equals(b)); \t\t\t\t\t// bad usage\n\t\tassertEquals(?a should equals b?, a, b);\t// good usage\n\t}\n}\n\n      "
    },
    "UseVarargs": {
        "title": "Consider using varargs for methods or constructors which take an array the last parameter.",
        "display_name": "UseVarargs",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Java 5 introduced the varargs parameter declaration for methods and constructors. This syntactic sugar provides flexibility for users of these methods and constructors, allowing them to avoid having to deal with the creation of an array.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UseVarargs\n\npublic class Foo {\n   public void foo(String s, Object[] args) {\n      // Do something here...\n   }\n\n   public void bar(String s, Object... args) {\n      // Ahh, varargs tastes much better...\n   }\n}\n        "
    },
    "AvoidUsingVolatile": {
        "title": "Use of modifier volatile is not recommended.",
        "display_name": "AvoidUsingVolatile",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use of the keyword 'volatile' is generally used to fine tune a Java application, and therefore, requires a good expertise of the Java Memory Model. Moreover, its range of action is somewhat misknown. Therefore, the volatile keyword should not be used for maintenance purpose and portability.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidUsingVolatile\n\n      \npublic class ThrDeux {\n  private volatile String var1;\t// not suggested\n  private          String var2;\t// preferred\n}\n      \n    "
    },
    "AvoidThrowingNewInstanceOfSameException": {
        "title": "A catch statement that catches an exception only to wrap it in a new instance of the same type of exception and throw it should be avoided",
        "display_name": "AvoidThrowingNewInstanceOfSameException",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Catch blocks that merely rethrow a caught exception wrapped inside a new instance of the same type only add to code size and runtime complexity.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidThrowingNewInstanceOfSameException\n  \npublic void bar() {\n      try {\n       // do something\n      }  catch (SomeException se) {\n         // harmless comment      \n           throw new SomeException(se);\n      }\n}\n  \n    "
    },
    "UselessStringValueOf": {
        "title": "No need to call String.valueOf to append to a string.",
        "display_name": "UselessStringValueOf",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "No need to call String.valueOf to append to a string; just use the valueOf() argument directly.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#UselessStringValueOf\n\n\npublic String convert(int i) {\n\tString s;\n\ts = \"a\" + String.valueOf(i);\t// not required\n\ts = \"a\" + i; \t\t\t\t\t// preferred approach\n\treturn s;\n}\n\n          "
    },
    "NoInlineStyleInformation": {
        "title": "Avoid having style information in JSP files.",
        "display_name": "NoInlineStyleInformation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Style information should be put in CSS files, not in JSPs. Therefore, don't use &lt;B> or &lt;FONT> tags, or attributes like \"align='center'\".\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoInlineStyleInformation\n\n\t\t\t\n<html><body><p align='center'><b>text</b></p></body></html>\n\t\t\t\n\t\t"
    },
    "ApexXSSFromURLParam": {
        "title": "Apex classes should escape/sanitize Strings obtained from URL parameters",
        "display_name": "ApexXSSFromURLParam",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Makes sure that all values obtained from URL parameters are properly escaped / sanitized to avoid XSS attacks.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexXSSFromURLParam\n\n            \npublic without sharing class Foo {\n    String unescapedstring = ApexPage.getCurrentPage().getParameters.get('url_param');\n    String usedLater = unescapedstring;\n}\n    \n        "
    },
    "NoClassAttribute": {
        "title": "Do not use an attribute called 'class'.",
        "display_name": "NoClassAttribute",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Do not use an attribute called 'class'. Use \"styleclass\" for CSS styles.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoClassAttribute\n\n\t\t\t\n<HTML> <BODY>\n<P class=\"MajorHeading\">Some text</P>\n</BODY> </HTML>\n\t\t\t\n\t\t"
    },
    "ApexSharingViolations": {
        "title": "Apex classes should declare a sharing model if DML or SOQL/SOSL is used",
        "display_name": "ApexSharingViolations",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detect classes declared without explicit sharing mode if DML methods are used. This forces the developer to take access restrictions into account before modifying objects.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexSharingViolations\n\n            \npublic without sharing class Foo {\n// DML operation here\n}\n    \n        "
    },
    "UnnecessaryFullyQualifiedName": {
        "title": "Unnecessary use of fully qualified name ''{0}'' due to existing {2}import ''{1}''",
        "display_name": "UnnecessaryFullyQualifiedName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Import statements allow the use of non-fully qualified names. The use of a fully qualified name which is covered by an import statement is redundant. Consider using the non-fully qualified name.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/imports.html#UnnecessaryFullyQualifiedName\n\nimport java.util.List;\n\npublic class Foo {\n   private java.util.List list1; // Unnecessary FQN\n   private List list2; // More appropriate given import of 'java.util.List'\n}\n\t\t  "
    },
    "ApexSOQLInjection": {
        "title": "Avoid untrusted/unescaped variables in DML query",
        "display_name": "ApexSOQLInjection",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects the usage of untrusted / unescaped variables in DML queries.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexSOQLInjection\n\n            \npublic class Foo {\n    public void test1(String t1) {\n        Database.query('SELECT Id FROM Account' + t1);\n    }\n}\n    \n        "
    },
    "UnsynchronizedStaticDateFormatter": {
        "title": "Static DateFormatter objects should be accessed in a synchronized manner",
        "display_name": "UnsynchronizedStaticDateFormatter",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "SimpleDateFormat instances are not synchronized. Sun recommends using separate format instances for each thread. If multiple threads must access a static formatter, the formatter must be synchronized either on method or block level.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UnsynchronizedStaticDateFormatter\n\n    \npublic class Foo {\n    private static final SimpleDateFormat sdf = new SimpleDateFormat();\n    void bar() {\n        sdf.format(); // poor, no thread-safety\n    }\n    synchronized void foo() {\n        sdf.format(); // preferred\n    }\n}\n    \n      "
    },
    "LoggerIsNotStaticFinal": {
        "title": "The Logger variable declaration does not contain the static and final modifiers",
        "display_name": "LoggerIsNotStaticFinal",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In most cases, the Logger reference can be declared as static and final.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-java.html#LoggerIsNotStaticFinal\n\n \npublic class Foo{\n    Logger log = Logger.getLogger(Foo.class.getName());\t\t\t\t\t// not recommended\n\n    static final Logger log = Logger.getLogger(Foo.class.getName());\t// preferred approach\n}\n\n     "
    },
    "StaticEJBFieldShouldBeFinal": {
        "title": "EJB's shouldn't have non-final static fields",
        "display_name": "StaticEJBFieldShouldBeFinal",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "According to the J2EE specification, an EJB should not have any static fields with write access. However, static read-only fields are allowed. This ensures proper behavior especially when instances are distributed by the container on several JREs.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#StaticEJBFieldShouldBeFinal\n\npublic class SomeEJB extends EJBObject implements EJBLocalHome {\n\n\tprivate static int CountA;\t\t\t// poor, field can be edited\n\n\tprivate static final int CountB;\t// preferred, read-only access\n}\n     "
    },
    "TooManyMethods": {
        "title": "This object has too many methods, consider refactoring it.",
        "display_name": "TooManyMethods",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A package or type with too many methods is probably a good suspect for refactoring, in order to reduce its complexity and find a way to have more fine grained objects.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#TooManyMethods\n"
    },
    "DontImportJavaLang": {
        "title": "Avoid importing anything from the package 'java.lang'",
        "display_name": "DontImportJavaLang",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid importing anything from the package 'java.lang'. These classes are automatically imported (JLS 7.5.3).\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/imports.html#DontImportJavaLang\n\n\nimport java.lang.String;\t// this is unnecessary\n\npublic class Foo {}\n\n// --- in another source code file...\n\nimport java.lang.*;\t// this is bad\n\npublic class Foo {}\n\n    "
    },
    "AssignmentToNonFinalStatic": {
        "title": "Possible unsafe assignment to a non-final static field in a constructor.",
        "display_name": "AssignmentToNonFinalStatic",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Identifies a possible unsafe usage of a static field.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AssignmentToNonFinalStatic\n\n   \npublic class StaticField {\n   static int x;\n   public FinalFields(int y) {\n    x = y; // unsafe\n   }\n}\n   \n       "
    },
    "CloneMethodMustImplementCloneable": {
        "title": "clone() method should be implemented only if implementing Cloneable interface",
        "display_name": "CloneMethodMustImplementCloneable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The method clone() should only be implemented if the class implements the Cloneable interface with the exception of a final method that only throws CloneNotSupportedException. This version uses PMD's type resolution facilities, and can detect if the class implements or extends a Cloneable class.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/typeresolution.html#CloneMethodMustImplementCloneable\n\n            \npublic class MyClass {\n\tpublic Object clone() throws CloneNotSupportedException {\n\t\treturn foo;\n\t}\n}\n   \n        "
    },
    "AvoidCallingFinalize": {
        "title": "Avoid calling finalize() explicitly",
        "display_name": "AvoidCallingFinalize",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The method Object.finalize() is called by the garbage collector on an object when garbage collection determines that there are no more references to the object. It should not be invoked by application logic.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/finalizers.html#AvoidCallingFinalize\n\n\nvoid foo() {\n\tBar b = new Bar();\n\tb.finalize();\n}\n\n      "
    },
    "DuplicateJspImports": {
        "title": "Avoid duplicate imports such as ''{0}''",
        "display_name": "DuplicateJspImports",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid duplicate import statements inside JSP's.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#DuplicateJspImports\n\n\t\t\t \n<%@ page import=\\\"com.foo.MyClass,com.foo.MyClass\\\"%><html><body><b><img src=\\\"<%=Some.get()%>/foo\\\">xx</img>text</b></body></html>\n\t\t\t \n\t\t"
    },
    "DoNotCallGarbageCollectionExplicitly": {
        "title": "Do not explicitly trigger a garbage collection.",
        "display_name": "DoNotCallGarbageCollectionExplicitly",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calls to System.gc(), Runtime.getRuntime().gc(), and System.runFinalization() are not advised. Code should have the same behavior whether the garbage collection is disabled using the option -Xdisableexplicitgc or not. Moreover, \"modern\" jvms do a very good job handling garbage collections. If memory usage issues unrelated to memory leaks develop within an application, it should be dealt with JVM options rather than within the code itself.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#DoNotCallGarbageCollectionExplicitly\n\n            \npublic class GCCall {\n    public GCCall() {\n        // Explicit gc call !\n        System.gc();\n    }\n\n    public void doSomething() {\n        // Explicit gc call !\n        Runtime.getRuntime().gc();\n    }\n\n    public explicitGCcall() {\n        // Explicit gc call !\n        System.gc();\n    }\n\n    public void doSomething() {\n        // Explicit gc call !\n        Runtime.getRuntime().gc();\n    }\n}\n      \n    "
    },
    "CouplingBetweenObjects": {
        "title": "High amount of different objects as members denotes a high coupling",
        "display_name": "CouplingBetweenObjects",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule counts the number of unique attributes, local variables, and return types within an object. A number higher than the specified threshold can indicate a high degree of coupling.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/coupling.html#CouplingBetweenObjects\n\n\nimport com.Blah;\nimport org.Bar;\nimport org.Bardo;\n\npublic class Foo {\n   private Blah var1;\n   private Bar var2;\n \n \t//followed by many imports of unique objects\n   void ObjectC doWork() {\n     Bardo var55;\n     ObjectA var44;\n     ObjectZ var93;\n     return something;\n   }\n}\n\n    "
    },
    "LocalInterfaceSessionNamingConvention": {
        "title": "The Local Interface of a Session EJB should be suffixed by 'Local'",
        "display_name": "LocalInterfaceSessionNamingConvention",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The Local Interface of a Session EJB should be suffixed by 'Local'.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#LocalInterfaceSessionNamingConvention\n\n            \n public interface MyLocal extends javax.ejb.EJBLocalObject {}\t\t\t\t// proper name\n\n public interface MissingProperSuffix extends javax.ejb.EJBLocalObject {}\t// non-standard name\n            \n        "
    },
    "ReplaceHashtableWithMap": {
        "title": "Consider replacing this Hashtable with the newer java.util.Map",
        "display_name": "ReplaceHashtableWithMap",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Consider replacing Hashtable usage with the newer java.util.Map if thread safety is not required.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#ReplaceHashtableWithMap\n\n    \npublic class Foo {\n\tvoid bar() {\n\t\tHashtable h = new Hashtable();\n\t}\n}\n    \n      "
    },
    "WhileLoopsMustUseBraces": {
        "title": "Avoid using 'while' statements without curly braces",
        "display_name": "WhileLoopsMustUseBraces",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using 'while' statements without using braces to surround the code block. If the code formatting or indentation is lost then it becomes difficult to separate the code being controlled from the rest.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/braces.html#WhileLoopsMustUseBraces\n\n\nwhile (true)\t// not recommended\n      x++;\n      \nwhile (true) {\t// preferred approach\n      x++;\n}\n\n      "
    },
    "ProperCloneImplementation": {
        "title": "Object clone() should be implemented with super.clone()",
        "display_name": "ProperCloneImplementation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Object clone() should be implemented with super.clone().\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/clone.html#ProperCloneImplementation\n\n \nclass Foo{\n    public Object clone(){\n        return new Foo(); // This is bad\n    }\n}\n\n     "
    },
    "RemoteSessionInterfaceNamingConvention": {
        "title": "Remote Home interface of a Session EJB should be suffixed by 'Home'",
        "display_name": "RemoteSessionInterfaceNamingConvention",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A Remote Home interface type of a Session EJB should be suffixed by 'Home'.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#RemoteSessionInterfaceNamingConvention\n\n            \npublic interface MyBeautifulHome extends javax.ejb.EJBHome {}\t\t// proper name\n\npublic interface MissingProperSuffix extends javax.ejb.EJBHome {}\t// non-standard name\n            \n        "
    },
    "RemoteInterfaceNamingConvention": {
        "title": "Remote Interface of a Session EJB should NOT be suffixed",
        "display_name": "RemoteInterfaceNamingConvention",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Remote Interface of a Session EJB should not have a suffix.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#RemoteInterfaceNamingConvention\n\n            \n /* Poor Session suffix */\n public interface BadSuffixSession extends javax.ejb.EJBObject {}\n\n /* Poor EJB suffix */\n public interface BadSuffixEJB extends javax.ejb.EJBObject {}\n\n /* Poor Bean suffix */\n public interface BadSuffixBean extends javax.ejb.EJBObject {}\n            \n        "
    },
    "FinalFieldCouldBeStatic": {
        "title": "This final field could be made static",
        "display_name": "FinalFieldCouldBeStatic",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If a final field is assigned to a compile-time constant, it could be made static, thus saving overhead in each object at runtime.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#FinalFieldCouldBeStatic\n\n  \npublic class Foo {\n  public final int BAR = 42; // this could be static and save some space\n}\n  \n      "
    },
    "InstantiationToGetClass": {
        "title": "Avoid instantiating an object just to call getClass() on it; use the .class public member instead",
        "display_name": "InstantiationToGetClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid instantiating an object just to call getClass() on it; use the .class public member instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#InstantiationToGetClass\n\n    \n  // replace this\nClass c = new String().getClass();\n\n  // with this:\nClass c = String.class;\n\n    \n        "
    },
    "EmptyTryBlock": {
        "title": "Avoid empty try blocks",
        "display_name": "EmptyTryBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid empty try blocks - what's the point?\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyTryBlock\n\n  \npublic class Foo {\n public void bar() {\n  try {\n  } catch (Exception e) {\n    e.printStackTrace();\n  }\n }\n}\n\n      "
    },
    "ApexSuggestUsingNamedCred": {
        "title": "Suggest named credentials for authentication",
        "display_name": "ApexSuggestUsingNamedCred",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects hardcoded credentials used in requests to an endpoint. You should refrain from hardcoding credentials: * They are hard to mantain by being mixed in application code * Particularly hard to update them when used from different classes * Granting a developer access to the codebase means granting knowledge of credentials, keeping a two-level access is not possible. * Using different credentials for different environments is troublesome and error-prone. Instead, you should use *Named Credentials* and a callout endpoint. For more information, you can check [this](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_callouts_named_credentials.htm)\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexSuggestUsingNamedCredRule\n\n            \npublic class Foo {\n    public void foo(String username, String password) {\n        Blob headerValue = Blob.valueOf(username + ':' + password);\n        String authorizationHeader = 'BASIC ' + EncodingUtil.base64Encode(headerValue);\n        req.setHeader('Authorization', authorizationHeader);\n    }\n}\n    \n        "
    },
    "UselessOverridingMethod": {
        "title": "Overriding method merely calls super",
        "display_name": "UselessOverridingMethod",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The overriding method merely calls the same method defined in a superclass.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UselessOverridingMethod\n\npublic void foo(String bar) {\n  super.foo(bar);      // why bother overriding?\n}\n\npublic String foo() {\n\treturn super.foo();  // why bother overriding?\n}\n\n@Id\npublic Long getId() {\n  return super.getId();  // OK if 'ignoreAnnotations' is false, which is the default behavior\n}\n        "
    },
    "AvoidDmlStatementsInLoops": {
        "title": "Avoid DML statements inside loops",
        "display_name": "AvoidDmlStatementsInLoops",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid DML statements inside loops to avoid hitting the DML governor limit. Instead, try to batch up the data into a list and invoke your DML once on that list of data outside the loop.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/performance.html#AvoidDmlStatementsInLoops\n\n\npublic class Something {\n\tpublic void foo() {  \n\t\tfor (Integer i = 0; i < 151; i++) {\n\t\t    Account account;\n\t\t    ...\n\t\t    insert account;\n\t\t}\n\t}\n}\n\n    "
    },
    "SuspiciousEqualsMethodName": {
        "title": "The method name and parameter number are suspiciously close to equals(Object)",
        "display_name": "SuspiciousEqualsMethodName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The method name and parameter number are suspiciously close to equals(Object), which can denote an intention to override the equals(Object) method.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#SuspiciousEqualsMethodName\n\npublic class Foo {\n   public int equals(Object o) {\n     // oops, this probably was supposed to be boolean equals\n   }\n   public boolean equals(String s) {\n     // oops, this probably was supposed to be equals(Object)\n   }\n   public boolean equals(Object o1, Object o2) {\n     // oops, this probably was supposed to be equals(Object)\n   }\n}\n        "
    },
    "TO_DATE_TO_CHAR": {
        "title": "TO_DATE(TO_CHAR(variable)) instead of TRUNC(variable)",
        "display_name": "TO_DATE_TO_CHAR",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "TO_DATE(TO_CHAR(date-variable)) used to remove time component - use TRUNC(date-veriable)\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/dates.html#TO_DATE_TO_CHAR\n\n\nCREATE OR REPLACE PACKAGE BODY date_utilities\nIS\n \n-- Take single parameter, relyimg on current default NLS date format \nFUNCTION strip_time (p_date IN DATE) RETURN DATE\nIS\nBEGIN\n   RETURN TO_DATE(TO_CHAR(p_date)); \nEND strip_time ;\n\n\nEND date_utilities ;\n/\n\n  "
    },
    "CollapsibleIfStatements": {
        "title": "These nested if statements could be combined",
        "display_name": "CollapsibleIfStatements",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Sometimes two consecutive 'if' statements can be consolidated by separating their conditions with a boolean short-circuit operator.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#CollapsibleIfStatements\n"
    },
    "LocalHomeNamingConvention": {
        "title": "The Local Home interface of a Session EJB should be suffixed by 'LocalHome'",
        "display_name": "LocalHomeNamingConvention",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The Local Home interface of a Session EJB should be suffixed by 'LocalHome'.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#LocalHomeNamingConvention\n\n            \n public interface MyBeautifulLocalHome extends javax.ejb.EJBLocalHome {}// proper name\n\n public interface MissingProperSuffix extends javax.ejb.EJBLocalHome {}\t// non-standard name\n            \n        "
    },
    "NoPackage": {
        "title": "All classes and interfaces must belong to a named package",
        "display_name": "NoPackage",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects when a class or interface does not have a package definition.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#NoPackage\n\n\n// no package declaration\npublic class ClassInDefaultPackage {\n}\n\n    "
    },
    "AvoidThrowingRawExceptionTypes": {
        "title": "Avoid throwing raw exception types.",
        "display_name": "AvoidThrowingRawExceptionTypes",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid throwing certain exception types. Rather than throw a raw RuntimeException, Throwable, Exception, or Error, use a subclassed exception or error instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidThrowingRawExceptionTypes\n\n      \npublic class Foo {\n  public void bar() throws Exception {\n    throw new Exception();\n   }\n}\n\n    "
    },
    "UseConcurrentHashMap": {
        "title": "If you run in Java5 or newer and have concurrent access, you should use the ConcurrentHashMap implementation",
        "display_name": "UseConcurrentHashMap",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Since Java5 brought a new implementation of the Map designed for multi-threaded access, you can perform efficient map reads without blocking other threads.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#UseConcurrentHashMap\n\n\npublic class ConcurrentApp {\n  public void getMyInstance() {\n    Map map1 = new HashMap(); \t// fine for single-threaded access\n    Map map2 = new ConcurrentHashMap();  // preferred for use with multiple threads\n\n    // the following case will be ignored by this rule\n    Map map3 = someModule.methodThatReturnMap(); // might be OK, if the returned map is already thread-safe\n  }\n}\n\n    "
    },
    "BeanMembersShouldSerialize": {
        "title": "Found non-transient, non-static member. Please mark as transient or provide accessors.",
        "display_name": "BeanMembersShouldSerialize",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If a class is a bean, or is referenced by a bean directly or indirectly it needs to be serializable. Member variables need to be marked as transient, static, or have accessor methods in the class. Marking variables as transient is the safest and easiest modification. Accessor methods should follow the Java naming conventions, i.e. for a variable named foo, getFoo() and setFoo() accessor methods should be provided.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/javabeans.html#BeanMembersShouldSerialize\n\n\nprivate transient int someFoo;  // good, it's transient\nprivate static int otherFoo;    // also OK\nprivate int moreFoo;            // OK, has proper accessors, see below\nprivate int badFoo;             // bad, should be marked transient\n\nprivate void setMoreFoo(int moreFoo){\n      this.moreFoo = moreFoo;\n}\n\nprivate int getMoreFoo(){\n      return this.moreFoo;\n}\n\n\n    "
    },
    "JUnitUseExpected": {
        "title": "In JUnit4, use the @Test(expected) annotation to denote tests that should throw exceptions",
        "display_name": "JUnitUseExpected",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In JUnit4, use the @Test(expected) annotation to denote tests that should throw exceptions.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#JUnitUseExpected\n\n\npublic class MyTest {\n\t@Test\n    public void testBad() {\n        try {\n            doSomething();\n            fail(\"should have thrown an exception\");\n        } catch (Exception e) {\n        }\n    }\n\n\t@Test(expected=Exception.class)\n    public void testGood() {\n        doSomething();\n    }\n}\n\n      "
    },
    "UncommentedEmptyMethodBody": {
        "title": "Document empty method body",
        "display_name": "UncommentedEmptyMethodBody",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Uncommented Empty Method Body finds instances where a method body does not contain statements, but there is no comment. By explicitly commenting empty method bodies it is easier to distinguish between intentional (commented) and unintentional empty methods.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UncommentedEmptyMethodBody\n\n  \npublic void doSomething() {\n}\n \n      "
    },
    "JUnitSpelling": {
        "title": "You may have misspelled a JUnit framework method (setUp or tearDown)",
        "display_name": "JUnitSpelling",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Some JUnit framework methods are easy to misspell.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#JUnitSpelling\n\n\nimport junit.framework.*;\n\npublic class Foo extends TestCase {\n   public void setup() {}    // oops, should be setUp\n   public void TearDown() {} // oops, should be tearDown\n}\n\n    "
    },
    "CloneMethodMustBePublic": {
        "title": "clone() method must be public if the class implements Cloneable",
        "display_name": "CloneMethodMustBePublic",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The java Manual says \"By convention, classes that implement this interface should override Object.clone (which is protected) with a public method.\"\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/clone.html#CloneMethodMustBePublic\n\n            \npublic class Foo implements Cloneable {\n    @Override\n    protected Object clone() throws CloneNotSupportedException { // Violation, must be public\n    }\n}\n\npublic class Foo implements Cloneable {\n    @Override\n    protected Foo clone() { // Violation, must be public\n    }\n}\n\npublic class Foo implements Cloneable {\n    @Override\n    public Object clone() // Ok\n}\n"
    },
    "SignatureDeclareThrowsException": {
        "title": "A method/constructor shouldn't explicitly throw java.lang.Exception",
        "display_name": "SignatureDeclareThrowsException",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "It is unclear which exceptions that can be thrown from the methods. It might be difficult to document and understand the vague interfaces. Use either a class derived from RuntimeException or a checked exception. JUnit classes are excluded.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/typeresolution.html#SignatureDeclareThrowsException\n\n      \t\npublic void methodThrowingException() throws Exception {\n}\n      \t\n      "
    },
    "DontUseFloatTypeForLoopIndices": {
        "title": "Don't use floating point for loop indices. If you must use floating point, use double.",
        "display_name": "DontUseFloatTypeForLoopIndices",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Don't use floating point for loop indices. If you must use floating point, use double unless you're certain that float provides enough precision and you have a compelling performance need (space or time).\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#DontUseFloatTypeForLoopIndices\n\n\npublic class Count {\n  public static void main(String[] args) {\n    final int START = 2000000000;\n    int count = 0;\n    for (float f = START; f < START + 50; f++)\n      count++;\n      //Prints 0 because (float) START == (float) (START + 50).\n      System.out.println(count);\n      //The termination test misbehaves due to floating point granularity.\n    }\n}\n\n    "
    },
    "InnaccurateNumericLiteral": {
        "title": "The numeric literal ''{0}'' will have at different value at runtime.",
        "display_name": "InnaccurateNumericLiteral",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The numeric literal will have at different value at runtime, which can happen if you provide too much precision in a floating point number. This may result in numeric calculations being in error.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#InnaccurateNumericLiteral\n\n  \nvar a = 9; // Ok\nvar b = 999999999999999; // Ok\nvar c = 999999999999999999999; // Not good\nvar w = 1.12e-4; // Ok\nvar x = 1.12; // Ok\nvar y = 1.1234567890123; // Ok\nvar z = 1.12345678901234567; // Not good\n\n      "
    },
    "FinalizeShouldBeProtected": {
        "title": "If you override finalize(), make it protected",
        "display_name": "FinalizeShouldBeProtected",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When overriding the finalize(), the new method should be set as protected. If made public, other classes may invoke it at inappropriate times.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/finalizers.html#FinalizeShouldBeProtected\n\n  \npublic void finalize() {\n\t// do something\n}\n  \n      "
    },
    "SimplifyConditional": {
        "title": "No need to check for null before an instanceof",
        "display_name": "SimplifyConditional",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "No need to check for null before an instanceof; the instanceof keyword returns false when given a null argument.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SimplifyConditional\n\n      \nclass Foo {\n  void bar(Object x) {\n    if (x != null && x instanceof Bar) {\n      // just drop the \"x != null\" check\n    }\n  }\n}      \n           "
    },
    "ReplaceVectorWithList": {
        "title": "Consider replacing this Vector with the newer java.util.List",
        "display_name": "ReplaceVectorWithList",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Consider replacing Vector usages with the newer java.util.ArrayList if expensive thread-safe operations are not required.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#ReplaceVectorWithList\n\n\npublic class Foo {\n void bar() {\n    Vector v = new Vector();\n }\n}\n\n  "
    },
    "ApexXSSFromEscapeFalse": {
        "title": "Apex classes should escape Strings in error messages",
        "display_name": "ApexXSSFromEscapeFalse",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Reports on calls to `addError` with disabled escaping. The message passed to `addError` will be displayed directly to the user in the UI, making it prime ground for XSS attacks if unescaped.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexXSSFromEscapeFalse\n\n            \npublic without sharing class Foo {\n    Trigger.new[0].addError(vulnerableHTMLGoesHere, false);\n}\n    \n        "
    },
    "OverrideBothEqualsAndHashcode": {
        "title": "Ensure you override both equals() and hashCode()",
        "display_name": "OverrideBothEqualsAndHashcode",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Override both public boolean Object.equals(Object other), and public int Object.hashCode(), or override neither. Even if you are inheriting a hashCode() from a parent class, consider implementing hashCode and explicitly delegating to your superclass.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#OverrideBothEqualsAndHashcode\n\n  \npublic class Bar {\t\t// poor, missing a hashcode() method\n\tpublic boolean equals(Object o) {\n      // do some comparison\n\t}\n}\n\npublic class Baz {\t\t// poor, missing an equals() method\n\tpublic int hashCode() {\n      // return some hash value\n\t}\n}\n\npublic class Foo {\t\t// perfect, both methods provided\n\tpublic boolean equals(Object other) {\n      // do some comparison\n\t}\n\tpublic int hashCode() {\n      // return some hash value\n\t}\n}\n \n      "
    },
    "ExcessivePublicCount": {
        "title": "This class has a bunch of public methods and attributes",
        "display_name": "ExcessivePublicCount",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Classes with large numbers of public methods and attributes require disproportionate testing efforts since combinational side effects grow rapidly and increase risk. Refactoring these classes into smaller ones not only increases testability and reliability but also allows new variations to be developed easily.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/codesize.html#ExcessivePublicCount\n\n    \npublic class Foo {\n\tpublic String value;\n\tpublic Bar something;\n\tpublic Variable var;\n // [... more more public attributes ...]\n \n\tpublic void doWork() {}\n\tpublic void doMoreWork() {}\n\tpublic void doWorkAgain() {}\n // [... more more public methods ...]\n}\n    \n    "
    },
    "AvoidLiteralsInIfCondition": {
        "title": "Avoid using Literals in Conditional Statements",
        "display_name": "AvoidLiteralsInIfCondition",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using hard-coded literals in conditional statements. By declaring them as static variables or private members with descriptive names maintainability is enhanced. By default, the literals \"-1\" and \"0\" are ignored. More exceptions can be defined with the property \"ignoreMagicNumbers\".\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidLiteralsInIfCondition\n\n\nprivate static final int MAX_NUMBER_OF_REQUESTS = 10;\n\npublic void checkRequests() {\n\n    if (i == 10) {                        // magic number, buried in a method\n      doSomething();\n    }\n\n    if (i == MAX_NUMBER_OF_REQUESTS) {    // preferred approach\n      doSomething();\n    }\n\n    if (aString.indexOf('.') != -1) {}     // magic number -1, by default ignored\n    if (aString.indexOf('.') >= 0) { }     // alternative approach\n\n    if (aDouble > 0.0) {}                  // magic number 0.0\n    if (aDouble >= Double.MIN_VALUE) {}    // preferred approach\n}\n\n    "
    },
    "ForLoopsMustUseBraces": {
        "title": "Avoid using 'for' statements without curly braces",
        "display_name": "ForLoopsMustUseBraces",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using 'for' statements without using curly braces. If the code formatting or indentation is lost then it becomes difficult to separate the code being controlled from the rest.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/braces.html#ForLoopsMustUseBraces\n\n\nfor (int i = 0; i < 42; i++)\n   foo();\n\n       "
    },
    "PrematureDeclaration": {
        "title": "Avoid declaring a variable if it is unreferenced before a possible exit point.",
        "display_name": "PrematureDeclaration",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Checks for variables that are defined before they might be used. A reference is deemed to be premature if it is created right before a block of code that doesn't use it that also has the ability to return or throw an exception.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#PrematureDeclaration\n\n              \npublic int getLength(String[] strings) {\n  \n  int length = 0;\t// declared prematurely\n\n  if (strings == null || strings.length == 0) return 0;\n  \n  for (String str : strings) {\n    length += str.length();\n    }\n\n  return length;\n}\n              \n              "
    },
    "JUnitAssertionsShouldIncludeMessage": {
        "title": "JUnit assertions should include a message",
        "display_name": "JUnitAssertionsShouldIncludeMessage",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "JUnit assertions should include an informative message - i.e., use the three-argument version of assertEquals(), not the two-argument version.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#JUnitAssertionsShouldIncludeMessage\n\n  \npublic class Foo extends TestCase {\n public void testSomething() {\n  assertEquals(\"foo\", \"bar\");\n  // Use the form:\n  // assertEquals(\"Foo does not equals bar\", \"foo\", \"bar\");\n  // instead\n }\n}\n  \n      "
    },
    "DontNestJsfInJstlIteration": {
        "title": "Do not nest JSF component custom actions inside a custom action that iterates over its body.",
        "display_name": "DontNestJsfInJstlIteration",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Do not nest JSF component custom actions inside a custom action that iterates over its body.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic-jsf.html#DontNestJsfInJstlIteration\n\n \n<html> <body> <ul>\n\t\t<c:forEach items='${books}' var='b'>\n\t\t\t<li> <h:outputText value='#{b}' /> </li>\n\t\t</c:forEach>\n</ul> </body> </html>\n \n     "
    },
    "DuplicateImports": {
        "title": "Avoid duplicate imports such as ''{0}''",
        "display_name": "DuplicateImports",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Duplicate or overlapping import statements should be avoided.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/imports.html#DuplicateImports\n\n\nimport java.lang.String;\nimport java.lang.*;\npublic class Foo {}\n\n    "
    },
    "ConstructorCallsOverridableMethod": {
        "title": "Overridable {0} called during object construction",
        "display_name": "ConstructorCallsOverridableMethod",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calling overridable methods during construction poses a risk of invoking methods on an incompletely constructed object and can be difficult to debug. It may leave the sub-class unable to construct its superclass or forced to replicate the construction process completely within itself, losing the ability to call super(). If the default constructor contains a call to an overridable method, the subclass may be completely uninstantiable. Note that this includes method calls throughout the control flow graph - i.e., if a constructor Foo() calls a private method bar() that calls a public method buz(), this denotes a problem.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#ConstructorCallsOverridableMethod\n\n  \npublic class SeniorClass {\n  public SeniorClass(){\n      toString(); //may throw NullPointerException if overridden\n  }\n  public String toString(){\n    return \"IAmSeniorClass\";\n  }\n}\npublic class JuniorClass extends SeniorClass {\n  private String name;\n  public JuniorClass(){\n    super(); //Automatic call leads to NullPointerException\n    name = \"JuniorClass\";\n  }\n  public String toString(){\n    return name.toUpperCase();\n  }\n}\n  \n      "
    },
    "LocalVariableCouldBeFinal": {
        "title": "Local variable ''{0}'' could be declared final",
        "display_name": "LocalVariableCouldBeFinal",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A local variable assigned only once can be declared final.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#LocalVariableCouldBeFinal\n\n  \npublic class Bar {\n\tpublic void foo () {\n\t\tString txtA = \"a\"; \t\t// if txtA will not be assigned again it is better to do this:\n\t\tfinal String txtB = \"b\";\n\t}\n}\n  \n      "
    },
    "AtLeastOneConstructor": {
        "title": "Each class should declare at least one constructor",
        "display_name": "AtLeastOneConstructor",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Each class should declare at least one constructor.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AtLeastOneConstructor\n\n  \npublic class Foo {\n   // missing constructor\n  public void doSomething() { ... }\n  public void doOtherThing { ... }\n}\n  \n  "
    },
    "NoScriptlets": {
        "title": "Avoid having scriptlets inside a JSP file.",
        "display_name": "NoScriptlets",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Scriptlets should be factored into Tag Libraries or JSP declarations, rather than being part of JSP pages.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoScriptlets\n\n\t\t\t \n<HTML>\n<HEAD>\n<%\nresponse.setHeader(\"Pragma\", \"No-cache\");\n%>\n</HEAD>\n\t<BODY>\n\t\t<jsp:scriptlet>String title = \"Hello world!\";</jsp:scriptlet>\n\t</BODY>\n</HTML>\n\t\t\t\t\t \n\t\t"
    },
    "ExcessiveClassLength": {
        "title": "Avoid really long classes.",
        "display_name": "ExcessiveClassLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Excessive class file lengths are usually indications that the class may be burdened with excessive responsibilities that could be provided by external classes or functions. In breaking these methods apart the code becomes more managable and ripe for reuse.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/codesize.html#ExcessiveClassLength\n\n\npublic class Foo {\n\tpublic void bar1() {\n    // 1000 lines of code\n\t}\n\tpublic void bar2() {\n    // 1000 lines of code\n\t}\n    public void bar3() {\n    // 1000 lines of code\n\t}\n\t\n\t\n    public void barN() {\n    // 1000 lines of code\n\t}\n}\n\n   "
    },
    "UseObjectForClearerAPI": {
        "title": "Rather than using a lot of String arguments, consider using a container object for those values.",
        "display_name": "UseObjectForClearerAPI",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When you write a public method, you should be thinking in terms of an API. If your method is public, it means other class will use it, therefore, you want (or need) to offer a comprehensive and evolutive API. If you pass a lot of information as a simple series of Strings, you may think of using an Object to represent all those information. You'll get a simpler API (such as doWork(Workload workload), rather than a tedious series of Strings) and more importantly, if you need at some point to pass extra data, you'll be able to do so by simply modifying or extending Workload without any modification to your API.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#UseObjectForClearerAPI\n\n\npublic class MyClass {\n  public void connect(String username,\n    String pssd,\n    String databaseName,\n    String databaseAdress)\n    // Instead of those parameters object\n    // would ensure a cleaner API and permit\n    // to add extra data transparently (no code change):\n    // void connect(UserData data);\n    {\n\n  }\n}\n\n    "
    },
    "ConsistentReturn": {
        "title": "A function should not mix 'return' statements with and without a result.",
        "display_name": "ConsistentReturn",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "ECMAScript does provide for return types on functions, and therefore there is no solid rule as to their usage. However, when a function does use returns they should all have a value, or all with no value. Mixed return usage is likely a bug, or at best poor style.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#ConsistentReturn\n\n  \n// Ok\nfunction foo() {\n   if (condition1) {\n      return true;\n   }\n   return false;\n}\n\n// Bad\nfunction bar() {\n   if (condition1) {\n      return;\n   }\n   return false;\n}\n\n      "
    },
    "DoNotHardCodeSDCard": {
        "title": "Do not hardcode /sdcard.",
        "display_name": "DoNotHardCodeSDCard",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use Environment.getExternalStorageDirectory() instead of \"/sdcard\"\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/android.html#DoNotHardCodeSDCard\n\n      \npublic class MyActivity extends Activity {\n\tprotected void foo() {\n\t\tString storageLocation = \"/sdcard/mypackage\";\t// hard-coded, poor approach\n\n\t\tstorageLocation = Environment.getExternalStorageDirectory() + \"/mypackage\"; // preferred approach\n\t}\n}\n\n    "
    },
    "UnreachableCode": {
        "title": "A ''return'', ''break'', ''continue'', or ''throw'' statement should be the last in a block.",
        "display_name": "UnreachableCode",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A 'return', 'break', 'continue', or 'throw' statement should be the last in a block. Statements after these will never execute. This is a bug, or extremely poor style.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#UnreachableCode\n\n  \n// Ok\nfunction foo() {\n   return 1;\n}\n// Bad\nfunction bar() {\n   var x = 1;\n   return x;\n   x = 2;\n}\n\n      "
    },
    "EmptyFinalizer": {
        "title": "Avoid empty finalize methods",
        "display_name": "EmptyFinalizer",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty finalize methods serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/finalizers.html#EmptyFinalizer\n\n\npublic class Foo {\n   protected void finalize() {}\n}\n\n       "
    },
    "FinalizeOnlyCallsSuperFinalize": {
        "title": "Finalize should do something besides just calling super.finalize()",
        "display_name": "FinalizeOnlyCallsSuperFinalize",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If the finalize() is implemented, it should do something besides just calling super.finalize().\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/finalizers.html#FinalizeOnlyCallsSuperFinalize\n\n           \nprotected void finalize() {\n\tsuper.finalize();\n}\n           \n       "
    },
    "StdCyclomaticComplexity": {
        "title": "The {0} ''{1}'' has a Standard Cyclomatic Complexity of {2}.",
        "display_name": "StdCyclomaticComplexity",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Complexity directly affects maintenance costs is determined by the number of decision points in a method plus one for the method entry. The decision points include 'if', 'while', 'for', and 'case labels' calls. Generally, numbers ranging from 1-4 denote low complexity, 5-7 denote moderate complexity, 8-10 denote high complexity, and 11+ is very high complexity.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/codesize.html#StdCyclomaticComplexity\n\n\npublic class Foo {    // This has a Cyclomatic Complexity = 12\n1   public void example()  {\n2       if (a == b || (c == d && e == f))  { // Only one\n3           if (a1 == b1) {\n                fiddle();\n4           } else if a2 == b2) {\n                fiddle();\n            }  else {\n                fiddle();\n            }\n5       } else if (c == d) {\n6           while (c == d) {\n                fiddle();\n            }\n7        } else if (e == f) {\n8           for (int n = 0; n < h; n++) {\n                fiddle();\n            }\n        } else{\n            switch (z) {\n9               case 1:\n                    fiddle();\n                    break;\n10              case 2:\n                    fiddle();\n                    break;\n11              case 3:\n                    fiddle();\n                    break;\n12              default:\n                    fiddle();\n                    break;\n            }\n        }\n    }\n}\n\n   "
    },
    "JUnit4TestShouldUseBeforeAnnotation": {
        "title": "JUnit 4 tests that set up tests should use the @Before annotation",
        "display_name": "JUnit4TestShouldUseBeforeAnnotation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In JUnit 3, the setUp method was used to set up all data entities required in running tests. JUnit 4 skips the setUp method and executes all methods annotated with @Before before all tests\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#JUnit4TestShouldUseBeforeAnnotation\n\n\npublic class MyTest {\n    public void setUp() {\n        bad();\n    }\n}\npublic class MyTest2 {\n    @Before public void setUp() {\n        good();\n    }\n}\n\n      "
    },
    "AvoidDeeplyNestedIfStmts": {
        "title": "Deeply nested if..then statements are hard to read",
        "display_name": "AvoidDeeplyNestedIfStmts",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid creating deeply nested if-then statements since they are harder to read and error-prone to maintain.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#AvoidDeeplyNestedIfStmts\n"
    },
    "ProperLogger": {
        "title": "Logger should be defined private static final and have the correct class",
        "display_name": "ProperLogger",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A logger should normally be defined private static final and be associated with the correct class. Private final Log log; is also allowed for rare cases where loggers need to be passed around, with the restriction that the logger needs to be passed into the constructor.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-jakarta-commons.html#ProperLogger\n\n \npublic class Foo {\n\n   private static final Log LOG = LogFactory.getLog(Foo.class);\t   // proper way\n\n   protected Log LOG = LogFactory.getLog(Testclass.class);\t\t\t// wrong approach\n}\n \n            "
    },
    "JUnit4TestShouldUseAfterAnnotation": {
        "title": "JUnit 4 tests that clean up tests should use the @After annotation",
        "display_name": "JUnit4TestShouldUseAfterAnnotation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In JUnit 3, the tearDown method was used to clean up all data entities required in running tests. JUnit 4 skips the tearDown method and executes all methods annotated with @After after running each test\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#JUnit4TestShouldUseAfterAnnotation\n\n\npublic class MyTest {\n    public void tearDown() {\n        bad();\n    }\n}\npublic class MyTest2 {\n    @After public void tearDown() {\n        good();\n    }\n}\n\n      "
    },
    "AvoidLosingExceptionInformation": {
        "title": "Avoid statements in a catch block that invoke accessors on the exception without using the information",
        "display_name": "AvoidLosingExceptionInformation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Statements in a catch block that invoke accessors on the exception without using the information only add to code size. Either remove the invocation, or use the return result.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidLosingExceptionInformation\n\n\npublic void bar() {\n\ttry {\n\t\t// do something\n\t} catch (SomeException se) {\n\t\tse.getMessage();\n\t}\n}\n\n\t\t"
    },
    "MethodWithSameNameAsEnclosingClass": {
        "title": "Classes should not have non-constructor methods with the same name as the class",
        "display_name": "MethodWithSameNameAsEnclosingClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Non-constructor methods should not have the same name as the enclosing class.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#MethodWithSameNameAsEnclosingClass\n\n    \npublic class MyClass {\n\n\tpublic MyClass() {}\t\t\t// this is OK because it is a constructor\n\t\n\tpublic void MyClass() {}\t// this is bad because it is a method\n}\n    \n       "
    },
    "FinalizeDoesNotCallSuperFinalize": {
        "title": "Last statement in finalize method should be a call to super.finalize()",
        "display_name": "FinalizeDoesNotCallSuperFinalize",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If the finalize() is implemented, its last action should be to call super.finalize.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/finalizers.html#FinalizeDoesNotCallSuperFinalize\n\n\nprotected void finalize() {\n\tsomething();\n\t// neglected to call super.finalize()\n}\n\n       "
    },
    "CyclomaticComplexity": {
        "title": "The {0} ''{1}'' has a Cyclomatic Complexity of {2}.",
        "display_name": "CyclomaticComplexity",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Complexity directly affects maintenance costs is determined by the number of decision points in a method plus one for the method entry. The decision points include 'if', 'while', 'for', and 'case labels' calls. Generally, numbers ranging from 1-4 denote low complexity, 5-7 denote moderate complexity, 8-10 denote high complexity, and 11+ is very high complexity.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#CyclomaticComplexity\n\n\n-- Cyclomatic Complexity of 25 \nCREATE OR REPLACE PACKAGE BODY pkg_pmd_working_sequence  AS \n1 PROCEDURE ty_logger  IS BEGIN\n2        IF true\n         THEN\n              DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n3\t\t IF true\n\t\t THEN\n\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n4\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n5\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n6\t\t ELSIF false\n\t\t THEN\n\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n7\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n8\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n\t\t ELSE\n\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n9\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n10\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n\t\t END IF;\n11         ELSIF false\n         THEN\n\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n12\t\t IF true\n\t\t THEN\n\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n13\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n14\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n15\t\t ELSIF false\n\t\t THEN\n16\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n17\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t ELSE\n\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t END IF;\n\t ELSE\n\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n18\t\t IF true\n\t\t THEN\n\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n19\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n20\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n21\t\t ELSIF false\n\t\t THEN\n\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n22\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n23\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n\t\t ELSE\n\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n24\t\t\t IF true\n\t\t\t THEN\n\t\t\t      DBMS_OUTPUT.PUT_LINE('IF/THEN l_Integer='||l_integer);         \n25\t\t\t ELSIF false\n\t\t\t THEN\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t ELSE\n\t\t\t\tDBMS_OUTPUT.PUT_LINE('ELSIF l_Integer='||l_integer);             \n\t\t\t END IF;\n\t\t END IF;\n\t END IF;\nEND;\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\nEND;\n\n   "
    },
    "GuardDebugLogging": {
        "title": "debug logging that involves string concatenation should be guarded with isDebugEnabled() checks",
        "display_name": "GuardDebugLogging",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When log messages are composed by concatenating strings, the whole section should be guarded by a isDebugEnabled() check to avoid performance and memory issues.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-jakarta-commons.html#GuardDebugLogging\n\n            \npublic class Test {\n    private static final Log __log = LogFactory.getLog(Test.class);\n    public void test() {\n        // okay:\n        __log.debug(\"log something\");\n\n        // okay:\n        __log.debug(\"log something with exception\", e);\n\n        // bad:\n        __log.debug(\"log something\" + \" and \" + \"concat strings\");\n\n        // bad:\n        __log.debug(\"log something\" + \" and \" + \"concat strings\", e);\n\n        // good:\n        if (__log.isDebugEnabled()) {\n        __log.debug(\"bla\" + \"\",e );\n        }\n    }\n}\n            \n        "
    },
    "ShortMethodName": {
        "title": "Avoid using short method names",
        "display_name": "ShortMethodName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Method names that are very short are not helpful to the reader.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#ShortMethodName\n\n\npublic class ShortMethod {\n\tpublic void a( int i ) { // Violation\n\t}\n}\n\n     "
    },
    "SingleMethodSingleton": {
        "title": "Class contains multiple getInstance methods. Please review.",
        "display_name": "SingleMethodSingleton",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Some classes contain overloaded getInstance. The problem with overloaded getInstance methods is that the instance created using the overloaded method is not cached and so, for each call and new objects will be created for every invocation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SingleMethodSingleton\n\npublic class Singleton {\n\n   private static Singleton singleton = new Singleton( );\n\n  private Singleton(){ }\n\npublic static Singleton getInstance( ) {\n\t  return singleton;\n}\npublic static Singleton getInstance(Object obj){\n\tSingleton singleton = (Singleton) obj;\n\treturn singleton;\t\t\t//violation\n}\n}\n\n"
    },
    "AvoidWithStatement": {
        "title": "Avoid using with - it's bad news",
        "display_name": "AvoidWithStatement",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using with - it's bad news\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#AvoidWithStatement\n\nwith (object) {\n  property = 3; // Might be on object, might be on window: who knows.\n}\n      "
    },
    "SimpleDateFormatNeedsLocale": {
        "title": "When instantiating a SimpleDateFormat object, specify a Locale",
        "display_name": "SimpleDateFormatNeedsLocale",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Be sure to specify a Locale when creating SimpleDateFormat instances to ensure that locale-appropriate formatting is used.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SimpleDateFormatNeedsLocale\n\n        \npublic class Foo {\n  // Should specify Locale.US (or whatever)\n  private SimpleDateFormat sdf = new SimpleDateFormat(\"pattern\");\n}\n        \n        "
    },
    "AvoidProtectedFieldInFinalClass": {
        "title": "Avoid protected fields in a final class.  Change to private or package access.",
        "display_name": "AvoidProtectedFieldInFinalClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Do not use protected fields in final classes since they cannot be subclassed. Clarify your intent by using private or package access modifiers instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AvoidProtectedFieldInFinalClass\n\n\npublic final class Bar {\n  private int x;\n  protected int y;  // bar cannot be subclassed, so is y really private or package visible?\n  Bar() {}\n}\n \n         "
    },
    "EmptyCatchBlock": {
        "title": "Avoid empty catch blocks",
        "display_name": "EmptyCatchBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty Catch Block finds instances where an exception is caught, but nothing is done. In most circumstances, this swallows an exception which should either be acted on or reported.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyCatchBlock\n\n  \npublic void doSomething() {\n  try {\n    FileInputStream fis = new FileInputStream(\"/tmp/bugger\");\n  } catch (IOException ioe) {\n      // not good\n  }\n}\n \n      "
    },
    "AddEmptyString": {
        "title": "Do not add empty strings",
        "display_name": "AddEmptyString",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The conversion of literals to strings by concatenating them with empty strings is inefficient. It is much better to use one of the type-specific toString() methods instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#AddEmptyString\n\n             \nString s = \"\" + 123; \t\t\t\t// inefficient \nString t = Integer.toString(456); \t// preferred approach\n            \n        "
    },
    "NcssObjectCount": {
        "title": "The Oracle object has an NCSS line count of {0}",
        "display_name": "NcssObjectCount",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule uses the NCSS (Non-Commenting Source Statements) algorithm to determine the number of lines of code for a given Oracle object. NCSS ignores comments, and counts actual statements. Using this algorithm, lines of code that are split are counted as one.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#NcssObjectCount\n\n\nCREATE OR REPLACE PACKAGE pkg_\n PROCEDURE Foo IS\n BEGIN\n --this class only has 6 NCSS lines\n     super();\n     super();\n END;\n}\n\n   "
    },
    "NcssConstructorCount": {
        "title": "The constructor with {0} parameters has an NCSS line count of {1}",
        "display_name": "NcssConstructorCount",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule uses the NCSS (Non-Commenting Source Statements) algorithm to determine the number of lines of code for a given constructor. NCSS ignores comments, and counts actual statements. Using this algorithm, lines of code that are split are counted as one.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/codesize.html#NcssConstructorCount\n\n\npublic class Foo extends Bar {\n public Foo() {\n     super();\n\n\n\n\n\n //this constructor only has 1 NCSS lines\n      super.foo();\n }\n}\n\n   "
    },
    "RedundantFieldInitializer": {
        "title": "Avoid using redundant field initializer for ''${variableName}''",
        "display_name": "RedundantFieldInitializer",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Java will initialize fields with known default values so any explicit initialization of those same defaults is redundant and results in a larger class file (approximately three additional bytecode instructions per field).\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#RedundantFieldInitializer\n\n              \npublic class C {\n\tboolean b\t= false;\t// examples of redundant initializers\n\tbyte by\t\t= 0;\n\tshort s\t\t= 0;\n\tchar c\t\t= 0;\n\tint i\t\t= 0;\n\tlong l\t\t= 0;\n\t\n\tfloat f\t\t= .0f;    // all possible float literals\n\tdoable d\t= 0d;     // all possible double literals\n\tObject o\t= null;\n\t\n\tMyClass mca[] = null;\n\tint i1 = 0, ia1[] = null;\n\t\n\tclass Nested {\n\t\tboolean b = false;\n\t}\n}\n              \n              "
    },
    "AssignmentInOperand": {
        "title": "Avoid assignments in operands",
        "display_name": "AssignmentInOperand",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid assignments in operands; this can make code more complicated and harder to read.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AssignmentInOperand\n\n  \npublic void bar() {\n    int x = 2;\n    if ((x = getX()) == 3) {\n      System.out.println(\"3!\");\n    }\n}\n  \n  "
    },
    "TO_DATEWithoutDateFormat": {
        "title": "TO_DATE without date format",
        "display_name": "TO_DATEWithoutDateFormat",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "TO_DATE without date format- use TO_DATE(expression, date-format)\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/dates.html#TO_DATEWithoutDateFormat\n\n\nCREATE OR REPLACE PACKAGE BODY date_utilities\nIS\n \n-- Take single parameter, relyimg on current default NLS date format \nFUNCTION to_date_single_parameter (p_date_string IN VARCHAR2) RETURN DATE\nIS\nBEGIN\n   RETURN TO_DATE(p_date_string); \nEND to_date_single_parameter ;\n\n-- Take 2 parameters, using an explicit date format string  \nFUNCTION to_date_two_parameters (p_date_string IN VARCHAR2, p_format_mask IN VARCHAR2) RETURN DATE\nIS\nBEGIN\n   TO_DATE(p_date_string, p_date_format); \nEND to_date_two_parameters ;\n\n-- Take 3 parameters, using an explicit date format string and an explicit language    \nFUNCTION to_date_three_parameters (p_date_string IN VARCHAR2, p_format_mask IN VARCHAR2, p_nls_language VARCHAR2 ) RETURN DATE\nIS\nBEGIN\n   TO_DATE(p_date_string, p_format_mask, p_nls_language); \nEND to_date_three_parameters ;\n\nEND date_utilities ;\n/\n\n  "
    },
    "AvoidUsingShortType": {
        "title": "Do not use the short type",
        "display_name": "AvoidUsingShortType",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Java uses the 'short' type to reduce memory usage, not to optimize calculation. In fact, the JVM does not have any arithmetic capabilities for the short type: the JVM must convert the short into an int, do the proper calculation and convert the int back to a short. Thus any storage gains found through use of the 'short' type may be offset by adverse impacts on performance.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidUsingShortType\n\n            \npublic class UsingShort {\n   private short doNotUseShort = 0;\n\n   public UsingShort() {\n    short shouldNotBeUsed = 1;\n    doNotUseShort += shouldNotBeUsed;\n  }\n}\n       \n     "
    },
    "NoUnsanitizedJSPExpression": {
        "title": "Using unsanitized JSP expression can lead to Cross Site Scripting (XSS) attacks",
        "display_name": "NoUnsanitizedJSPExpression",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using expressions without escaping / sanitizing. This could lead to cross site scripting - as the expression would be interpreted by the browser directly (e.g. \"<script>alert('hello');</script>\").\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoUnsanitizedJSPExpression\n\n            \n<%@ page contentType=\"text/html; charset=UTF-8\" %>\n<%@ taglib prefix=\"fn\" uri=\"http://java.sun.com/jsp/jstl/functions\" %>\n${expression}                    <!-- don't use this -->\n${fn:escapeXml(expression)}      <!-- instead, escape it -->\n<c:out value=\"${expression}\" />  <!-- or use c:out -->\n            \n        "
    },
    "ApexOpenRedirect": {
        "title": "Apex classes should safely redirect to a known location",
        "display_name": "ApexOpenRedirect",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Checks against redirects to user-controlled locations. This prevents attackers from redirecting users to phishing sites.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexOpenRedirect\n\n            \npublic without sharing class Foo {\n    String unsafeLocation = ApexPage.getCurrentPage().getParameters.get('url_param');\n    PageReference page() {\n       return new PageReference(unsafeLocation);\n    }\n}\n    \n        "
    },
    "UseIndexOfChar": {
        "title": "String.indexOf(char) is faster than String.indexOf(String).",
        "display_name": "UseIndexOfChar",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use String.indexOf(char) when checking for the index of a single character; it executes faster.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#UseIndexOfChar\n\n\nString s = \"hello world\";\n  // avoid this\nif (s.indexOf(\"d\") {}\n  // instead do this\nif (s.indexOf('d') {}\n\n    "
    },
    "GlobalVariable": {
        "title": "Avoid using global variables",
        "display_name": "GlobalVariable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule helps to avoid using accidently global variables by simply missing the \"var\" declaration. Global variables can lead to side-effects that are hard to debug.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#GlobalVariable\n\n\nfunction(arg) {\n    notDeclaredVariable = 1; // this will create a global variable and trigger the rule\n\n    var someVar = 1; // this is a local variable, that's ok\n\n    window.otherGlobal = 2; // this will not trigger the rule, although it is a global variable.\n}\n\n        "
    },
    "ApexCRUDViolation": {
        "title": "Validate CRUD permission before SOQL/DML operation",
        "display_name": "ApexCRUDViolation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The rule validates you are checking for access permissions before a SOQL/SOSL/DML operation. Since Apex runs in system mode not having proper permissions checks results in escalation of privilege and may produce runtime errors. This check forces you to handle such scenarios.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexCRUDViolationRule\n\n            \npublic class Foo {\n    public Contact foo(String status, String ID) {\n        Contact c = [SELECT Status__c FROM Contact WHERE Id=:ID];\n\n        // Make sure we can update the database before even trying\n        if (!Schema.sObjectType.Contact.fields.Name.isUpdateable()) {\n            return null;\n        }\n\n        c.Status__c = status;\n        update c;\n        return c;\n    }\n}\n    \n        "
    },
    "IframeMissingSrcAttribute": {
        "title": "IFrames must have a src attribute.",
        "display_name": "IframeMissingSrcAttribute",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "IFrames which are missing a src element can cause security information popups in IE if you are accessing the page through SSL. See http://support.microsoft.com/default.aspx?scid=kb;EN-US;Q261188\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#IframeMissingSrcAttribute\n\n\t\t\t\n<HTML><title>bad example><BODY>\n<iframe></iframe>\n</BODY> </HTML>\n\n<HTML><title>good example><BODY>\n<iframe src=\"foo\"></iframe>\n</BODY> </HTML>\n\t\t\t\n\t\t"
    },
    "MisleadingVariableName": {
        "title": "Avoid naming non-fields with the prefix 'm_'",
        "display_name": "MisleadingVariableName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects when a non-field has a name starting with 'm_'. This usually denotes a field and could be confusing.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#MisleadingVariableName\n\n  \npublic class Foo {\n    private int m_foo; // OK\n    public void bar(String m_baz) {  // Bad\n      int m_boz = 42; // Bad\n    }\n}\n  \n      "
    },
    "SingletonClassReturningNewInstance": {
        "title": "getInstance method always creates a new object and hence does not comply to Singleton Design Pattern behaviour. Please review",
        "display_name": "SingletonClassReturningNewInstance",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Some classes contain overloaded getInstance. The problem with overloaded getInstance methods is that the instance created using the overloaded method is not cached and so, for each call and new objects will be created for every invocation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SingletonClassReturningNewInstance\n\nclass Singleton {\n\tprivate static Singleton instance = null;\n\tpublic static Singleton getInstance() {\n\tsynchronized(Singleton.class){\n\t\treturn new Singleton();\n\t}\n\t}\n}\n\n"
    },
    "MDBAndSessionBeanNamingConvention": {
        "title": "SessionBean or MessageBean should be suffixed by Bean",
        "display_name": "MDBAndSessionBeanNamingConvention",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The EJB Specification states that any MessageDrivenBean or SessionBean should be suffixed by 'Bean'.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#MDBAndSessionBeanNamingConvention\n\n            \npublic class SomeBean implements SessionBean{}\t\t\t\t\t// proper name\n\npublic class MissingTheProperSuffix implements SessionBean {}  \t// non-standard name\n            \n        "
    },
    "TooManyStaticImports": {
        "title": "Too many static imports may lead to messy code",
        "display_name": "TooManyStaticImports",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If you overuse the static import feature, it can make your program unreadable and unmaintainable, polluting its namespace with all the static members you import. Readers of your code (including you, a few months after you wrote it) will not know which class a static member comes from (Sun 1.5 Language Guide).\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/imports.html#TooManyStaticImports\n\nimport static Lennon;\nimport static Ringo;\nimport static George;\nimport static Paul;\nimport static Yoko; // Too much !\n\t\t  "
    },
    "AvoidInstantiatingObjectsInLoops": {
        "title": "Avoid instantiating new objects inside loops",
        "display_name": "AvoidInstantiatingObjectsInLoops",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "New objects created within loops should be checked to see if they can created outside them and reused.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#AvoidInstantiatingObjectsInLoops\n\n\npublic class Something {\n\tpublic static void main( String as[] ) {  \n\t\tfor (int i = 0; i < 10; i++) {\n\t\t    Foo f = new Foo(); // Avoid this whenever you can it's really expensive\n\t\t}\n\t}\n}\n\n    "
    },
    "AvoidBranchingStatementAsLastInLoop": {
        "title": "Avoid using a branching statement as the last in a loop.",
        "display_name": "AvoidBranchingStatementAsLastInLoop",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Using a branching statement as the last part of a loop may be a bug, and/or is confusing. Ensure that the usage is not a bug, or consider using another approach.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#AvoidBranchingStatementAsLastInLoop\n\n            \n  // unusual use of branching statement in a loop\nfor (int i = 0; i < 10; i++) {\n\tif (i*i <= 25) {\n\t\tcontinue;\n\t}\n\tbreak;\n}\n\n  // this makes more sense...\nfor (int i = 0; i < 10; i++) {\n\tif (i*i > 25) {\n\t\tbreak;\n\t}\n}\n            \n        "
    },
    "NonCaseLabelInSwitchStatement": {
        "title": "A non-case label was present in a switch statement",
        "display_name": "NonCaseLabelInSwitchStatement",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A non-case label (e.g. a named break/continue label) was present in a switch statement. This legal, but confusing. It is easy to mix up the case labels and the non-case labels.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#NonCaseLabelInSwitchStatement\n\n   \npublic class Foo {\n  void bar(int a) {\n   switch (a) {\n     case 1:\n       // do something\n       break;\n     mylabel: // this is legal, but confusing!\n       break;\n     default:\n       break;\n    }\n  }\n}\n   \n       "
    },
    "CommentDefaultAccessModifier": {
        "title": "Missing commented default access modifier",
        "display_name": "CommentDefaultAccessModifier",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "To avoid mistakes if we want that a Method, Field or Nested class have a default access modifier we must add a comment at the beginning of the Method, Field or Nested class. By default the comment must be /* default */, if you want another, you have to provide a regex.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/comments.html#CommentDefaultAccessModifier\n\n        \n        public class Foo {\n            final String stringValue = \"some string\";\n            String getString() {\n               return stringValue;\n            }\n\n            class NestedFoo {\n            }\n        }\n\n        // should be\n        public class Foo {\n            /* default */ final String stringValue = \"some string\";\n            /* default */ String getString() {\n               return stringValue;\n            }\n\n            /* default */ class NestedFoo {\n            }\n        }\n        \n    "
    },
    "DoubleCheckedLocking": {
        "title": "Double checked locking is not thread safe in Java.",
        "display_name": "DoubleCheckedLocking",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Partially created objects can be returned by the Double Checked Locking pattern when used in Java. An optimizing JRE may assign a reference to the baz variable before it calls the constructor of the object the reference points to. Note: With Java 5, you can make Double checked locking work, if you declare the variable to be `volatile`. For more details refer to: http://www.javaworld.com/javaworld/jw-02-2001/jw-0209-double.html or http://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#DoubleCheckedLocking\n\n  \npublic class Foo {\n\t/*volatile */ Object baz = null; // fix for Java5 and later: volatile\n\tObject bar() {\n\t\tif (baz == null) { // baz may be non-null yet not fully created\n\t\t\tsynchronized(this) {\n\t\t\t\tif (baz == null) {\n\t\t\t\t\tbaz = new Object();\n        \t\t}\n      \t\t}\n    \t}\n\t\treturn baz;\n\t}\n}\n \n      "
    },
    "AppendCharacterWithChar": {
        "title": "Avoid appending characters as strings in StringBuffer.append.",
        "display_name": "AppendCharacterWithChar",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid concatenating characters as strings in StringBuffer/StringBuilder.append methods.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#AppendCharacterWithChar\n\n\nStringBuffer sb = new StringBuffer();\nsb.append(\"a\");\t\t // avoid this\n\nStringBuffer sb = new StringBuffer();\nsb.append('a');\t\t// use this instead\n\n    "
    },
    "ConfusingTernary": {
        "title": "Avoid if (x != y) ..; else ..;",
        "display_name": "ConfusingTernary",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid negation within an \"if\" expression with an \"else\" clause. For example, rephrase: if (x != y) diff(); else same(); as: if (x == y) same(); else diff(); Most \"if (x != y)\" cases without an \"else\" are often return cases, so consistent use of this rule makes the code easier to read. Also, this resolves trivial ordering problems, such as \"does the error case go first?\" or \"does the common case go first?\".\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#ConfusingTernary\n\n          \nboolean bar(int x, int y) {\n  return (x != y) ? diff : same;\n }\n          \n        "
    },
    "AvoidProtectedMethodInFinalClassNotExtending": {
        "title": "Avoid protected methods in a final class that doesn't extend anything other than Object.  Change to private or package access.",
        "display_name": "AvoidProtectedMethodInFinalClassNotExtending",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Do not use protected methods in most final classes since they cannot be subclassed. This should only be allowed in final classes that extend other classes with protected methods (whose visibility cannot be reduced). Clarify your intent by using private or package access modifiers instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AvoidProtectedMethodInFinalClassNotExtending\n\n\npublic final class Foo {\n  private int bar() {}\n  protected int baz() {} // Foo cannot be subclassed, and doesn't extend anything, so is baz() really private or package visible?\n}\n \n         "
    },
    "UnnecessaryBooleanAssertion": {
        "title": "assertTrue(true) or similar statements are unnecessary",
        "display_name": "UnnecessaryBooleanAssertion",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A JUnit test assertion with a boolean literal is unnecessary since it always will evaluate to the same thing. Consider using flow control (in case of assertTrue(false) or similar) or simply removing statements like assertTrue(true) and assertFalse(false). If you just want a test to halt after finding an error, use the fail() method and provide an indication message of why it did.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#UnnecessaryBooleanAssertion\n\n\npublic class SimpleTest extends TestCase {\n\tpublic void testX() {\n\t\tassertTrue(true);\t\t // serves no real purpose\n\t}\n}\n\n          "
    },
    "AvoidGlobalModifier": {
        "title": "Avoid using global modifier",
        "display_name": "AvoidGlobalModifier",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Global classes should be avoided (especially in managed packages) as they can never be deleted or changed in signature. Always check twice if something needs to be global. Many interfaces (e.g. Batch) required global modifiers in the past but don't require this anymore. Don't lock yourself in.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/style.html#AvoidGlobalModifier\n\nglobal class Unchangeable {\n\tglobal UndeletableType unchangable(UndeletableType param) {\n\t\t// ...\n\t}\n}\n\n    "
    },
    "ShortVariable": {
        "title": "Avoid variables with short names like {0}",
        "display_name": "ShortVariable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Fields, local variables, or parameter names that are very short are not helpful to the reader.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#ShortVariable\n\n\npublic class Something {\n    private int q = 15;                         // field - too short\n    public static void main( String as[] ) {    // formal arg - too short\n        int r = 20 + q;                         // local var - too short\n        for (int i = 0; i < 10; i++) {          // not a violation (inside 'for' loop)\n            r += q;\n        }\n        for (Integer i : numbers) {             // not a violation (inside 'for-each' loop)\n            r += q;\n        }\n    }\n}\n\n    "
    },
    "PositionLiteralsFirstInCaseInsensitiveComparisons": {
        "title": "Position literals first in String comparisons for EqualsIgnoreCase",
        "display_name": "PositionLiteralsFirstInCaseInsensitiveComparisons",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Position literals first in comparisons, if the second argument is null then NullPointerExceptions can be avoided, they will just return false.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#PositionLiteralsFirstInCaseInsensitiveComparisons\n\n\nclass Foo {\n  boolean bar(String x) {\n    return x.equalsIgnoreCase(\"2\"); // should be \"2\".equalsIgnoreCase(x)\n  }\n}\n\n\n  "
    },
    "IfElseStmtsMustUseBraces": {
        "title": "Avoid using 'if...else' statements without curly braces",
        "display_name": "IfElseStmtsMustUseBraces",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using if..else statements without using surrounding braces. If the code formatting or indentation is lost then it becomes difficult to separate the code being controlled from the rest.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/braces.html#IfElseStmtsMustUseBraces\n\n\n   // this is OK\nif (foo) x++;\n   \n   // but this is not\nif (foo)\n       x = x+1;\n   else\n       x = x-1;\n\n       "
    },
    "FinalizeOverloaded": {
        "title": "Finalize methods should not be overloaded",
        "display_name": "FinalizeOverloaded",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Methods named finalize() should not have parameters. It is confusing and most likely an attempt to overload Object.finalize(). It will not be called by the VM.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/finalizers.html#FinalizeOverloaded\n\n\npublic class Foo {\n   // this is confusing and probably a bug\n   protected void finalize(int a) {\n   }\n}\n\n   "
    },
    "GuardLogStatement": {
        "title": "There is log block not surrounded by if",
        "display_name": "GuardLogStatement",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Whenever using a log level, one should check if the loglevel is actually enabled, or otherwise skip the associate String creation and manipulation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-jakarta-commons.html#GuardLogStatement\n\n \n    // Add this for performance\n    if (log.isDebugEnabled() { ...\n        log.debug(\"log something\" + \" and \" + \"concat strings\");\n\n     "
    },
    "IfStmtsMustUseBraces": {
        "title": "Avoid using if statements without curly braces",
        "display_name": "IfStmtsMustUseBraces",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using if statements without using braces to surround the code block. If the code formatting or indentation is lost then it becomes difficult to separate the code being controlled from the rest.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/braces.html#IfStmtsMustUseBraces\n\n \n\nif (foo)\t// not recommended\n\tx++;\n\nif (foo) {\t// preferred approach\n\tx++;\n}\n\n \n     "
    },
    "ClassWithOnlyPrivateConstructorsShouldBeFinal": {
        "title": "A class which only has private constructors should be final",
        "display_name": "ClassWithOnlyPrivateConstructorsShouldBeFinal",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A class with only private constructors should be final, unless the private constructor is invoked by a inner class.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#ClassWithOnlyPrivateConstructorsShouldBeFinal\n\npublic class Foo {  //Should be final\n    private Foo() { }\n}\n     "
    },
    "UncommentedEmptyConstructor": {
        "title": "Document empty constructor",
        "display_name": "UncommentedEmptyConstructor",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Uncommented Empty Constructor finds instances where a constructor does not contain statements, but there is no comment. By explicitly commenting empty constructors it is easier to distinguish between intentional (commented) and unintentional empty constructors.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UncommentedEmptyConstructor\n\n  \npublic Foo() {\n  // This constructor is intentionally empty. Nothing special is needed here.\n}\n \n      "
    },
    "InefficientEmptyStringCheck": {
        "title": "String.trim().length()==0 is an inefficient way to validate an empty String.",
        "display_name": "InefficientEmptyStringCheck",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "String.trim().length() is an inefficient way to check if a String is really empty, as it creates a new String object just to check its size. Consider creating a static function that loops through a string, checking Character.isWhitespace() on each character and returning false if a non-whitespace character is found. You can refer to Apache's StringUtils#isBlank (in commons-lang) or Spring's StringUtils#hasText (in the Springs framework) for existing implementations.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#InefficientEmptyStringCheck\n\n\npublic void bar(String string) {\n\tif (string != null && string.trim().size() > 0) {\n\t\tdoSomething();\n\t}\n}\n\n    "
    },
    "ExcessiveTypeLength": {
        "title": "Avoid really long Object Type specifications ({0} lines found).",
        "display_name": "ExcessiveTypeLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Excessive class file lengths are usually indications that the class may be burdened with excessive responsibilities that could be provided by external classes or functions. In breaking these methods apart the code becomes more managable and ripe for reuse.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#ExcessiveTypeLength\n\n\nCREATE OR REPLACE\nTYPE BODY Foo AS\n\t MEMBER PROCEDURE bar1 IS BEGIN\n    -- 1000 lines of code\n\tEND bar1;\n\t MEMBER PROCEDURE bar2 IS BEGIN\n    -- 1000 lines of code\n\tEND bar2;\n     MEMBER PROCEDURE bar3 IS BEGIN\n    -- 1000 lines of code\n\tEND bar3;\n\t\n\t\n     MEMBER PROCEDURE barN IS BEGIN\n    -- 1000 lines of code\n\tEND barn;\nEND;\n\n   "
    },
    "UseArraysAsList": {
        "title": "Use asList instead of tight loops",
        "display_name": "UseArraysAsList",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The java.util.Arrays class has a \"asList\" method that should be used when you want to create a new List from an array of objects. It is faster than executing a loop to copy all the elements of the array one by one.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#UseArraysAsList\n\n   \npublic class Test {\n  public void foo(Integer[] ints) {\n    // could just use Arrays.asList(ints)\n     List l= new ArrayList(10);\n     for (int i=0; i< 100; i++) {\n       l.add(ints[i]);\n     }\n     for (int i=0; i< 100; i++) {\n       l.add(a[i].toString()); // won't trigger the rule\n     }\n  }\n}\n   \n     "
    },
    "InvalidDependencyTypes": {
        "title": "By default, Maven only recognized the following types: $validTypes.",
        "display_name": "InvalidDependencyTypes",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "While Maven will not failed if you use an invalid type for a dependency in the dependency management section, it will not also uses the dependency.\nhttps://pmd.github.io/pmd-5.8.1/pmd-xml/rules/pom/basic.html#InvalidDependencyTypes\n\n \n<project...>\n  ...\n  <dependencyManagement>\n      ...\n    <dependency>\n      <groupId>org.jboss.arquillian</groupId>\n      <artifactId>arquillian-bom</artifactId>\n      <version>${arquillian.version}</version>\n      <type>bom</type> <!-- not a valid type ! 'pom' is ! -->\n      <scope>import</scope>\n    </dependency>\n    ...\n  </dependencyManagement>\n</project>\n \n     "
    },
    "SimplifyStartsWith": {
        "title": "This call to String.startsWith can be rewritten using String.charAt(0)",
        "display_name": "SimplifyStartsWith",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Since it passes in a literal of length 1, calls to (string).startsWith can be rewritten using (string).charAt(0) at the expense of some readability.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#SimplifyStartsWith\n\n  \npublic class Foo {\n\n\tboolean checkIt(String x) {\n\t\treturn x.startsWith(\"a\");\t// suboptimal\n\t}\n  \n\tboolean fasterCheckIt(String x) {\n\t\treturn x.charAt(0) == 'a';\t//\tfaster approach\n\t}\n}\n\n      "
    },
    "DefaultLabelNotLastInSwitchStmt": {
        "title": "The default label should be the last label in a switch statement",
        "display_name": "DefaultLabelNotLastInSwitchStmt",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "By convention, the default label should be the last label in a switch statement.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#DefaultLabelNotLastInSwitchStmt\n\n   \npublic class Foo {\n  void bar(int a) {\n   switch (a) {\n    case 1:  // do something\n       break;\n    default:  // the default case should be last, by convention\n       break;\n    case 2:\n       break;\n   }\n  }\n}   \n       "
    },
    "ModifiedCyclomaticComplexity": {
        "title": "The {0} ''{1}'' has a Modified Cyclomatic Complexity of {2}.",
        "display_name": "ModifiedCyclomaticComplexity",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Complexity directly affects maintenance costs is determined by the number of decision points in a method plus one for the method entry. The decision points include 'if', 'while', 'for', and 'case labels' calls. Generally, numbers ranging from 1-4 denote low complexity, 5-7 denote moderate complexity, 8-10 denote high complexity, and 11+ is very high complexity. Modified complexity treats switch statements as a single decision point.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/codesize.html#ModifiedCyclomaticComplexity\n\n\npublic class Foo {    // This has a Cyclomatic Complexity = 9\n1   public void example()  {\n2       if (a == b)  {\n3           if (a1 == b1) {\n                fiddle();\n4           } else if a2 == b2) {\n                fiddle();\n            }  else {\n                fiddle();\n            }\n5       } else if (c == d) {\n6           while (c == d) {\n                fiddle();\n            }\n7        } else if (e == f) {\n8           for (int n = 0; n < h; n++) {\n                fiddle();\n            }\n        } else{\n9           switch (z) {\n                case 1:\n                    fiddle();\n                    break;\n                case 2:\n                    fiddle();\n                    break;\n                case 3:\n                    fiddle();\n                    break;\n                default:\n                    fiddle();\n                    break;\n            }\n        }\n    }\n}\n\n   "
    },
    "NonThreadSafeSingleton": {
        "title": "Singleton is not thread safe",
        "display_name": "NonThreadSafeSingleton",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Non-thread safe singletons can result in bad state changes. Eliminate static singletons if possible by instantiating the object directly. Static singletons are usually not needed as only a single instance exists anyway. Other possible fixes are to synchronize the entire method or to use an [initialize-on-demand holder class](https://en.wikipedia.org/wiki/Initialization-on-demand_holder_idiom). Refrain from using the double-checked locking pattern. The Java Memory Model doesn't guarantee it to work unless the variable is declared as `volatile`, adding an uneeded performance penalty. [Reference](http://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html) See Effective Java, item 48.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#NonThreadSafeSingleton\n\nprivate static Foo foo = null;\n\n//multiple simultaneous callers may see partially initialized objects\npublic static Foo getFoo() {\n    if (foo==null) {\n        foo = new Foo();\n    }\n    return foo;\n}\n        "
    },
    "ApexInsecureEndpoint": {
        "title": "Apex callouts should use encrypted communication channels",
        "display_name": "ApexInsecureEndpoint",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Checks against accessing endpoints under plain **http**. You should always use **https** for security.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexInsecureEndpoint\n\n            \npublic without sharing class Foo {\n    void foo() {\n        HttpRequest req = new HttpRequest();\n        req.setEndpoint('http://localhost:com');\n    }\n}\n    \n        "
    },
    "ApexDangerousMethods": {
        "title": "Calling potentially dangerous method",
        "display_name": "ApexDangerousMethods",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Checks against calling dangerous methods. For the time being, it reports: * Against `FinancialForce`'s `Configuration.disableTriggerCRUDSecurity()`. Disabling CRUD security opens the door to several attacks and requires manual validation, which is unreliable. * Calling `System.debug` passing sensitive data as parameter, which could lead to exposure of private data.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/security.html#ApexDangerousMethodsRule\n\n            \npublic class Foo {\n    public Foo() {\n        Configuration.disableTriggerCRUDSecurity();\n    }\n}\n    \n        "
    },
    "JumbledIncrementer": {
        "title": "Avoid modifying an outer loop incrementer in an inner loop for update expression",
        "display_name": "JumbledIncrementer",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid jumbled loop incrementers - its usually a mistake, and is confusing even if intentional.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#JumbledIncrementer\n\n \npublic class JumbledIncrementerRule1 {\n\tpublic void foo() {\n\t\tfor (int i = 0; i < 10; i++) {\t\t\t// only references 'i'\n\t\t\tfor (int k = 0; k < 20; i++) {\t\t// references both 'i' and 'k'\n\t\t\t\tSystem.out.println(\"Hello\");\n\t\t\t}\n\t\t}\n\t}\n}\n \n     "
    },
    "EmptyForeachStmt": {
        "title": "Avoid empty foreach loops",
        "display_name": "EmptyForeachStmt",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty foreach statements should be deleted.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#EmptyForeachStmt\n"
    },
    "InvalidSlf4jMessageFormat": {
        "title": "Invalid message format",
        "display_name": "InvalidSlf4jMessageFormat",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Check for messages in slf4j loggers with non matching number of arguments and placeholders.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-java.html#InvalidSlf4jMessageFormat\n\n                \nLOGGER.error(\"forget the arg {}\");\nLOGGER.error(\"too many args {}\", \"arg1\", \"arg2\");\nLOGGER.error(\"param {}\", \"arg1\", new IllegalStateException(\"arg\")); //The exception is shown separately, so is correct.\n\n     "
    },
    "CallSuperInConstructor": {
        "title": "It is a good practice to call super() in a constructor",
        "display_name": "CallSuperInConstructor",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "It is a good practice to call super() in a constructor. If super() is not called but another constructor (such as an overloaded constructor) is called, this rule will not report it.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#CallSuperInConstructor\n\n\npublic class Foo extends Bar{\n  public Foo() {\n   // call the constructor of Bar\n   super();\n  }\n public Foo(int code) {\n  // do something with code\n   this();\n   // no problem with this\n  }\n}\n\n      "
    },
    "UseProperClassLoader": {
        "title": "In J2EE, getClassLoader() might not work as expected.  Use Thread.currentThread().getContextClassLoader() instead.",
        "display_name": "UseProperClassLoader",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In J2EE, the getClassLoader() method might not work as expected. Use Thread.currentThread().getContextClassLoader() instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#UseProperClassLoader\n\n\npublic class Foo {\n ClassLoader cl = Bar.class.getClassLoader();\n}\n\n  "
    },
    "JspEncoding": {
        "title": "JSP file should use UTF-8 encoding",
        "display_name": "JspEncoding",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A missing 'meta' tag or page directive will trigger this rule, as well as a non-UTF-8 charset.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#JspEncoding\n\n\t\t\t\n                Most browsers should be able to interpret the following headers:\n                \n                <%@ page contentType=\"text/html; charset=UTF-8\" pageEncoding=\"UTF-8\" %>\n                    \n                <meta http-equiv=\"Content-Type\"  content=\"text/html; charset=UTF-8\" />\n            \n\t\t"
    },
    "PositionLiteralsFirstInComparisons": {
        "title": "Position literals first in String comparisons",
        "display_name": "PositionLiteralsFirstInComparisons",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Position literals first in comparisons, if the second argument is null then NullPointerExceptions can be avoided, they will just return false.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#PositionLiteralsFirstInComparisons\n\n\nclass Foo {\n  boolean bar(String x) {\n    return x.equals(\"2\"); // should be \"2\".equals(x)\n  }\n}\n\n\n  "
    },
    "DoNotUseThreads": {
        "title": "To be compliant to J2EE, a webapp should not use any thread.",
        "display_name": "DoNotUseThreads",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The J2EE specification explicitly forbids the use of threads.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#DoNotUseThreads\n\n            \t\n            // This is not allowed\npublic class UsingThread extends Thread {\n\n }\n\t// Neither this,\npublic class OtherThread implements Runnable {\n\t// Nor this ...\n\tpublic void methode() {\n\t\t\tRunnable thread = new Thread(); thread.run();\n\t}\n}\n\t\t\t\t\n\t\t"
    },
    "UseAssertSameInsteadOfAssertTrue": {
        "title": "Use assertSame(x, y) instead of assertTrue(x==y), or assertNotSame(x,y) vs assertFalse(x==y)",
        "display_name": "UseAssertSameInsteadOfAssertTrue",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule detects JUnit assertions in object references equality. These assertions should be made by more specific methods, like assertSame, assertNotSame.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#UseAssertSameInsteadOfAssertTrue\n\n\npublic class FooTest extends TestCase {\n void testCode() {\n  Object a, b;\n  assertTrue(a == b); // bad usage\n  assertSame(a, b);  // good usage\n }\n}\n\n      "
    },
    "ExceptionAsFlowControl": {
        "title": "Avoid using exceptions as flow control.",
        "display_name": "ExceptionAsFlowControl",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Using Exceptions as form of flow control is not recommended as they obscure true exceptions when debugging. Either add the necessary validation or use an alternate control structure.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#ExceptionAsFlowControl\n\n  \npublic void bar() {\n    try {\n      try {\n      } catch (Exception e) {\n        throw new WrapperException(e);\n       // this is essentially a GOTO to the WrapperException catch block\n       }\n     } catch (WrapperException e) {\n     // do some more stuff\n    }\n  }\n  \n      "
    },
    "DoNotExtendJavaLangError": {
        "title": "Exceptions should not extend java.lang.Error",
        "display_name": "DoNotExtendJavaLangError",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Errors are system exceptions. Do not extend them.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#DoNotExtendJavaLangError\n\npublic class Foo extends Error { }\n    "
    },
    "AvoidUsingOctalValues": {
        "title": "Do not start a literal by 0 unless it's an octal value",
        "display_name": "AvoidUsingOctalValues",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Integer literals should not start with zero since this denotes that the rest of literal will be interpreted as an octal value.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#AvoidUsingOctalValues\n\n\t\t    \nint i = 012;\t// set i with 10 not 12\nint j = 010;\t// set j with 8 not 10\nk = i * j;\t\t// set k with 80 not 120\n\t\t    \n    "
    },
    "ImmutableField": {
        "title": "Private field ''{0}'' could be made final; it is only initialized in the declaration or constructor.",
        "display_name": "ImmutableField",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Identifies private fields whose values never change once they are initialized either in the declaration of the field or by a constructor. This helps in converting existing classes to becoming immutable ones.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#ImmutableField\n\n  \npublic class Foo {\n  private int x; // could be final\n  public Foo() {\n      x = 7;\n  }\n  public void foo() {\n     int a = x + 2;\n  }\n}\n  \n      "
    },
    "SwitchStmtsShouldHaveDefault": {
        "title": "Switch statements should have a default label",
        "display_name": "SwitchStmtsShouldHaveDefault",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "All switch statements should include a default option to catch any unspecified values.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SwitchStmtsShouldHaveDefault\n\n\npublic void bar() {\n    int x = 2;\n    switch (x) {\n      case 1: int j = 6;\n      case 2: int j = 8;\n      \t\t\t\t// missing default: here\n    }\n}\n\n    "
    },
    "EmptyWhileStmt": {
        "title": "Avoid empty 'while' statements",
        "display_name": "EmptyWhileStmt",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty While Statement finds all instances where a while statement does nothing. If it is a timing loop, then you should use Thread.sleep() for it; if it is a while loop that does a lot in the exit expression, rewrite it to make it clearer.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyWhileStmt\n\n  \nvoid bar(int a, int b) {\n\twhile (a == b) {\n\t// empty!\n\t}\n}\n \n       "
    },
    "ExcessiveMethodLength": {
        "title": "Avoid really long methods ({0} lines found).",
        "display_name": "ExcessiveMethodLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When methods are excessively long this usually indicates that the method is doing more than its name/signature might suggest. They also become challenging for others to digest since excessive scrolling causes readers to lose focus. Try to reduce the method length by creating helper methods and removing any copy/pasted code.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#ExcessiveMethodLength\n\n\nCREATE OR REPLACE\nPROCEDURE doSomething BEGIN\n\tDBMS_OUTPUT.PUT_LINE(\"Hello world!\");\n\tDBMS_OUTPUT.PUT_LINE(\"Hello world!\");\n\t\t-- 98 copies omitted for brevity.\nEND;\n\n\n   "
    },
    "AbstractClassWithoutAnyMethod": {
        "title": "No abstract method which means that the keyword is most likely used to prevent instantiation. Use a private or protected constructor instead.",
        "display_name": "AbstractClassWithoutAnyMethod",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If an abstract class does not provides any methods, it may be acting as a simple data container that is not meant to be instantiated. In this case, it is probably better to use a private or protected constructor in order to prevent instantiation than make the class misleadingly abstract.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AbstractClassWithoutAnyMethod\n\n            \npublic class abstract Example {\n\tString field;\n\tint otherField;\n}\n            \n        "
    },
    "NoInlineJavaScript": {
        "title": "Avoid inline JavaScript",
        "display_name": "NoInlineJavaScript",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid inline JavaScript. Import .js files instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#NoInlineJavaScript\n"
    },
    "VariableNamingConventions": {
        "title": "{0} variable {1} should begin with {2}",
        "display_name": "VariableNamingConventions",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A variable naming conventions rule - customize this to your liking. Currently, it checks for final variables that should be fully capitalized and non-final variables that should not include underscores.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#VariableNamingConventions\n\n\npublic class Foo {\n   public static final int MY_NUM = 0;\n   public String myTest = \"\";\n   DataModule dmTest = new DataModule();\n}\n\n        "
    },
    "UseLocaleWithCaseConversions": {
        "title": "When doing a String.toLowerCase()/toUpperCase() call, use a Locale",
        "display_name": "UseLocaleWithCaseConversions",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When doing String.toLowerCase()/toUpperCase() conversions, use Locales to avoids problems with languages that have unusual conventions, i.e. Turkish.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UseLocaleWithCaseConversions\n\n    \nclass Foo {\n // BAD\n if (x.toLowerCase().equals(\"list\")) { }\n /*\n This will not match \"LIST\" when in Turkish locale\n The above could be\n if (x.toLowerCase(Locale.US).equals(\"list\")) { }\n or simply\n if (x.equalsIgnoreCase(\"list\")) { }\n */\n // GOOD\n String z = a.toLowerCase(Locale.EN);\n}\n    \n        "
    },
    "MissingStaticMethodInNonInstantiatableClass": {
        "title": "Class cannot be instantiated and does not provide any static methods or fields",
        "display_name": "MissingStaticMethodInNonInstantiatableClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A class that has private constructors and does not have any static methods or fields cannot be used.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#MissingStaticMethodInNonInstantiatableClass\n\n\n// This class is unusable, since it cannot be\n// instantiated (private constructor),\n// and no static method can be called.\n\npublic class Foo {\n  private Foo() {}\n  void foo() {}\n}\n\n\n      "
    },
    "NoJspForward": {
        "title": "Do not do a forward from within a JSP file.",
        "display_name": "NoJspForward",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Do not do a forward from within a JSP file.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoJspForward\n\n\t\t\t\n<jsp:forward page='UnderConstruction.jsp'/>\n\t\t\t\n\t\t"
    },
    "AvoidAxisNavigation": {
        "title": "Axis navigation has the largest impact when writing an XPath query.",
        "display_name": "AvoidAxisNavigation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using the 'following' or 'preceeding' axes whenever possible, as these can cut through 100% of the document in the worst case. Also, try to avoid using 'descendant' or 'descendant-self' axes, as if you're at the top of the Document, it necessarily means cutting through 100% of the document.\nhttps://pmd.github.io/pmd-5.8.1/pmd-xml/rules/xsl/xpath.html#AvoidAxisNavigation\n\n \n <xsl:variable name=\"var\" select=\"//item/descendant::child\"/>\n \n     "
    },
    "JUnitTestsShouldIncludeAssert": {
        "title": "JUnit tests should include assert() or fail()",
        "display_name": "JUnitTestsShouldIncludeAssert",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "JUnit tests should include at least one assertion. This makes the tests more robust, and using assert with messages provide the developer a clearer idea of what the test does.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#JUnitTestsShouldIncludeAssert\n\n    \npublic class Foo extends TestCase {\n   public void testSomething() {\n      Bar b = findBar();\n   // This is better than having a NullPointerException\n   // assertNotNull(\"bar not found\", b);\n   b.work();\n   }\n}\n    \n        "
    },
    "NoLongScripts": {
        "title": "Avoid having long scripts (e.g. Javascript) inside a JSP file.",
        "display_name": "NoLongScripts",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Scripts should be part of Tag Libraries, rather than part of JSP pages.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoLongScripts\n\n\t\t\t\n<HTML>\n<BODY>\n<!--Java Script-->\n<SCRIPT language=\"JavaScript\" type=\"text/javascript\">\n<!--\nfunction calcDays(){\n  var date1 = document.getElementById('d1').lastChild.data;\n  var date2 = document.getElementById('d2').lastChild.data;\n  date1 = date1.split(\"-\");\n  date2 = date2.split(\"-\");\n  var sDate = new Date(date1[0]+\"/\"+date1[1]+\"/\"+date1[2]);\n  var eDate = new Date(date2[0]+\"/\"+date2[1]+\"/\"+date2[2]);\n  var daysApart = Math.abs(Math.round((sDate-eDate)/86400000));\n  document.getElementById('diffDays').lastChild.data = daysApart;\n}\n\nonload=calcDays;\n//-->\n</SCRIPT>\n</BODY>\n</HTML>\n\t\t\t\n\t\t"
    },
    "ApexUnitTestShouldNotUseSeeAllDataTrue": {
        "title": "Apex unit tests should not use @isTest(seeAllData = true)",
        "display_name": "ApexUnitTestShouldNotUseSeeAllDataTrue",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Apex unit tests should not use @isTest(seeAllData=true) because it opens up the existing database data for unexpected modification by tests.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/apexunit.html#ApexUnitTestShouldNotUseSeeAllDataTrue\n\n            \n@isTest(seeAllData = true)\npublic class Foo {\n   public static testMethod void testSomething() {\n      Account a = null;\n   // This is better than having a NullPointerException\n   // System.assertNotEquals(a, null, 'account not found');\n   a.toString();\n   }\n}\n    \n        "
    },
    "LongVariable": {
        "title": "Avoid excessively long variable names like {0}",
        "display_name": "LongVariable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Fields, formal arguments, or local variable names that are too long can make the code difficult to follow.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#LongVariable\n\n\npublic class Something {\n\tint reallyLongIntName = -3;  \t\t\t// VIOLATION - Field\n\tpublic static void main( String argumentsList[] ) { // VIOLATION - Formal\n\t\tint otherReallyLongName = -5; \t\t// VIOLATION - Local\n\t\tfor (int interestingIntIndex = 0;\t// VIOLATION - For\n             interestingIntIndex < 10;\n             interestingIntIndex ++ ) {\n    }\n}\n\n    "
    },
    "CommentContent": {
        "title": "Invalid words or phrases found",
        "display_name": "CommentContent",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A rule for the politically correct... we don't want to offend anyone.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/comments.html#CommentContent\n\n      \n//\tOMG, this is horrible, Bob is an idiot !!!\n      \n  "
    },
    "ShortInstantiation": {
        "title": "Avoid instantiating Short objects. Call Short.valueOf() instead",
        "display_name": "ShortInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calling new Short() causes memory allocation that can be avoided by the static Short.valueOf(). It makes use of an internal cache that recycles earlier instances making it more memory efficient.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#ShortInstantiation\n\n\npublic class Foo {\n\tprivate Short i = new Short(0); // change to Short i = Short.valueOf(0);\n}\n\n          "
    },
    "MethodArgumentCouldBeFinal": {
        "title": "Parameter ''{0}'' is not assigned and could be declared final",
        "display_name": "MethodArgumentCouldBeFinal",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A method argument that is never re-assigned within the method can be declared final.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#MethodArgumentCouldBeFinal\n\n  \npublic void foo1 (String param) {\t// do stuff with param never assigning it\n  \n}\n\npublic void foo2 (final String param) {\t// better, do stuff with param never assigning it\n  \n}\n  \n      "
    },
    "CloneMethodReturnTypeMustMatchClassName": {
        "title": "The return type of the clone() method must be the class name when implements Cloneable",
        "display_name": "CloneMethodReturnTypeMustMatchClassName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "If a class implements cloneable the return type of the method clone() must be the class name. That way, the caller of the clone method doesn't need to cast the returned clone to the correct type. Note: This is only possible with Java 1.5 or higher.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/clone.html#CloneMethodReturnTypeMustMatchClassName\n\n            \npublic class Foo implements Cloneable {\n    @Override\n    protected Object clone() { // Violation, Object must be Foo\n    }\n}\n\npublic class Foo implements Cloneable {\n    @Override\n    public Foo clone() { //Ok\n    }\n}\n            \n        "
    },
    "UselessParentheses": {
        "title": "Useless parentheses.",
        "display_name": "UselessParentheses",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Useless parentheses should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UselessParentheses\n\n    \npublic class Foo {\n\n   private int _bar1;\n   private Integer _bar2;\n\n   public void setBar(int n) {\n      _bar1 = Integer.valueOf((n)); // here\n      _bar2 = (n); // and here\n   }\n\n}\n    \n    "
    },
    "UnnecessaryBlock": {
        "title": "Unnecessary block.",
        "display_name": "UnnecessaryBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "An unnecessary Block is present. Such Blocks are often used in other languages to introduce a new variable scope. Blocks do not behave like this in ECMAScipt, and using them can be misleading. Considering removing this unnecessary Block.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/unnecessary.html#UnnecessaryBlock\n\n    \nif (foo) {\n   // Ok\n}\nif (bar) {\n   {\n      // Bad\n   }\n}\n    \n    "
    },
    "PreserveStackTrace": {
        "title": "New exception is thrown in catch block, original stack trace may be lost",
        "display_name": "PreserveStackTrace",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Throwing a new exception from a catch block without passing the original exception into the new exception will cause the original stack trace to be lost making it difficult to debug effectively.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#PreserveStackTrace\n\n    \npublic class Foo {\n    void good() {\n        try{\n            Integer.parseInt(\"a\");\n        } catch (Exception e) {\n            throw new Exception(e); // first possibility to create exception chain\n        }\n        try {\n            Integer.parseInt(\"a\");\n        } catch (Exception e) {\n            throw (IllegalStateException)new IllegalStateException().initCause(e); // second possibility to create exception chain.\n        }\n    }\n    void bad() {\n        try{\n            Integer.parseInt(\"a\");\n        } catch (Exception e) {\n            throw new Exception(e.getMessage());\n        }\n    }\n}\n    \n      "
    },
    "UnnecessaryLocalBeforeReturn": {
        "title": "Consider simply returning the value vs storing it in local variable ''{0}''",
        "display_name": "UnnecessaryLocalBeforeReturn",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid the creation of unnecessary local variables\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UnnecessaryLocalBeforeReturn\n\n  \npublic class Foo {\n   public int foo() {\n     int x = doSomething();\n     return x;  // instead, just 'return doSomething();'\n   }\n}\n  \n      "
    },
    "DoNotCallSystemExit": {
        "title": "System.exit() should not be used in J2EE/JEE apps",
        "display_name": "DoNotCallSystemExit",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Web applications should not call System.exit(), since only the web container or the application server should stop the JVM. This rule also checks for the equivalent call Runtime.getRuntime().exit().\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/j2ee.html#DoNotCallSystemExit\n\n    \t\t\npublic void bar() {\n    System.exit(0);                 // never call this when running in an application server!\n}\npublic void foo() {\n    Runtime.getRuntime().exit(0);   // never stop the JVM manually, the container will do this.\n}\n     "
    },
    "AvoidThreadGroup": {
        "title": "Avoid using java.lang.ThreadGroup; it is not thread safe",
        "display_name": "AvoidThreadGroup",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using java.lang.ThreadGroup; although it is intended to be used in a threaded environment it contains methods that are not thread-safe.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#AvoidThreadGroup\n\n    \npublic class Bar {\n\tvoid buz() {\n\t\tThreadGroup tg = new ThreadGroup(\"My threadgroup\") ;\n\t\ttg = new ThreadGroup(tg, \"my thread group\");\n\t\ttg = Thread.currentThread().getThreadGroup();\n\t\ttg = System.getSecurityManager().getThreadGroup();\n\t}\n}\n    \n      "
    },
    "SystemPrintln": {
        "title": "{0} is used",
        "display_name": "SystemPrintln",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "References to System.(out|err).print are usually intended for debugging purposes and can remain in the codebase even in production code. By using a logger one can enable/disable this behaviour at will (and by priority) and avoid clogging the Standard out log.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/logging-java.html#SystemPrintln\n\n \nclass Foo{\n    Logger log = Logger.getLogger(Foo.class.getName());\n    public void testA () {\n        System.out.println(\"Entering test\");\n        // Better use this\n        log.fine(\"Entering test\");\n    }\n}\n\n     "
    },
    "ScopeForInVariable": {
        "title": "The for-in loop variable ''{0}'' should be explicitly scoped with 'var' to avoid pollution.",
        "display_name": "ScopeForInVariable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A for-in loop in which the variable name is not explicitly scoped to the enclosing scope with the 'var' keyword can refer to a variable in an enclosing scope outside the nearest enclosing scope. This will overwrite the existing value of the variable in the outer scope when the body of the for-in is evaluated. When the for-in loop has finished, the variable will contain the last value used in the for-in, and the original value from before the for-in loop will be gone. Since the for-in variable name is most likely intended to be a temporary name, it is better to explicitly scope the variable name to the nearest enclosing scope with 'var'.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#ScopeForInVariable\n\n  \n// Ok\nfunction foo() {\n   var p = 'clean';\n   function() {\n\t   var obj = { dirty: 'dirty' };\n\t   for (var p in obj) { // Use 'var' here.\n\t     obj[p] = obj[p];\n\t   }\n\t   return x;\n   }();\n\n   // 'p' still has value of 'clean'.\n}\n// Bad\nfunction bar() {\n   var p = 'clean';\n   function() {\n\t   var obj = { dirty: 'dirty' };\n\t   for (p in obj) { // Oh no, missing 'var' here!\n\t     obj[p] = obj[p];\n\t   }\n\t   return x;\n   }();\n\n   // 'p' is trashed and has value of 'dirty'!\n}\n\n      "
    },
    "LogicInversion": {
        "title": "Use opposite operator instead of the logic complement operator.",
        "display_name": "LogicInversion",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use opposite operator instead of negating the whole expression with a logic complement operator.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#LogicInversion\n\n    \npublic boolean bar(int a, int b) {\n\n    if (!(a == b)) { // use !=\n         return false;\n     }\n\n    if (!(a < b)) { // use >=\n         return false;\n    }\n\n    return true;\n}\n    \n    "
    },
    "JUnit4TestShouldUseTestAnnotation": {
        "title": "JUnit 4 tests that execute tests should use the @Test annotation",
        "display_name": "JUnit4TestShouldUseTestAnnotation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In JUnit 3, the framework executed all methods which started with the word test as a unit test. In JUnit 4, only methods annotated with the @Test annotation are executed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#JUnit4TestShouldUseTestAnnotation\n\n\npublic class MyTest {\n    public void testBad() {\n        doSomething();\n    }\n\n\t@Test\n    public void testGood() {\n        doSomething();\n    }\n}\n\n      "
    },
    "UseEqualsToCompareStrings": {
        "title": "Use equals() to compare strings instead of ''=='' or ''!=''",
        "display_name": "UseEqualsToCompareStrings",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Using '==' or '!=' to compare strings only works if intern version is used on both sides. Use the equals() method instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#UseEqualsToCompareStrings\n\n\npublic boolean test(String s) {\n    if (s == \"one\") return true; \t\t// unreliable\n    if (\"two\".equals(s)) return true; \t// better\n    return false;\n}\n\n    "
    },
    "LoosePackageCoupling": {
        "title": "Use of ''{0}'' outside of package hierarchy ''{1}'' is not recommended; use recommended classes instead",
        "display_name": "LoosePackageCoupling",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using classes from the configured package hierarchy outside of the package hierarchy, except when using one of the configured allowed classes.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/coupling.html#LoosePackageCoupling\n\n\npackage some.package;\n\nimport some.other.package.subpackage.subsubpackage.DontUseThisClass;\n\npublic class Bar {\n   DontUseThisClass boo = new DontUseThisClass();\n}\n  \n      "
    },
    "ExcessiveImports": {
        "title": "A high number of imports can indicate a high degree of coupling within an object.",
        "display_name": "ExcessiveImports",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A high number of imports can indicate a high degree of coupling within an object. This rule counts the number of unique imports and reports a violation if the count is above the user-specified threshold.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/coupling.html#ExcessiveImports\n\n      \nimport blah.blah.Baz;\nimport blah.blah.Bif;\n// 18 others from the same package elided\npublic class Foo {\n public void doWork() {}\n}\n      \n  "
    },
    "UnusedNullCheckInEquals": {
        "title": "Invoke equals() on the object you''ve already ensured is not null",
        "display_name": "UnusedNullCheckInEquals",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "After checking an object reference for null, you should invoke equals() on that object rather than passing it to another object's equals() method.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UnusedNullCheckInEquals\n\n\t\t\npublic class Test {\n\n  public String method1() { return \"ok\";}\n  public String method2() { return null;}\n\n  public void method(String a) {\n    String b;\n\t// I don't know it method1() can be \"null\"\n\t// but I know \"a\" is not null..\n\t// I'd better write a.equals(method1())\n\t\n\tif (a!=null && method1().equals(a)) { // will trigger the rule\n\t//whatever\n\t}\n\t\n\tif (method1().equals(a) && a != null) { // won't trigger the rule\n\t//whatever\n\t}\n\t\n\tif (a!=null && method1().equals(b)) { // won't trigger the rule\n\t//whatever\n\t}\n\t\n\tif (a!=null && \"LITERAL\".equals(a)) { // won't trigger the rule\n\t//whatever\n\t}\n\t\n\tif (a!=null && !a.equals(\"go\")) { // won't trigger the rule\n\ta=method2();\n\tif (method1().equals(a)) {\n\t//whatever\n\t}\n  }\n}\n}\n\t\t\t\t\n\t\t\t"
    },
    "UseConcatOnce": {
        "title": "The xpath concat() function accepts as many arguments as required, you may be able to factorize this expression",
        "display_name": "UseConcatOnce",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The XPath concat() functions accepts as many arguments as required so you can have \"concat($a,'b',$c)\" rather than \"concat($a,concat('b',$c)\".\nhttps://pmd.github.io/pmd-5.8.1/pmd-xml/rules/xsl/xpath.html#UseConcatOnce\n\n \n <xsl:variable name=\"var\" select=\"concat(\"Welcome\",concat(\"to you \",$name))\"/>\n <xsl:variable name=\"var\" select=\"concat(\"Welcome\",\"to you \",$name))\">\n \n     "
    },
    "AvoidRethrowingException": {
        "title": "A catch statement that catches an exception only to rethrow it should be avoided.",
        "display_name": "AvoidRethrowingException",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Catch blocks that merely rethrow a caught exception only add to code size and runtime complexity.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidRethrowingException\n  \npublic void bar() {\n    try {\n    // do something\n    }  catch (SomeException se) {\n       throw se;\n    }\n}\n  \n    "
    },
    "MethodNamingConventions": {
        "title": "Method name does not begin with a lower case character.",
        "display_name": "MethodNamingConventions",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Method names should always begin with a lower case character, and should not contain underscores.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#MethodNamingConventions\n\n\npublic class Foo {\n\tpublic void fooStuff() {\n\t}\n}\n\n          "
    },
    "UselessOperationOnImmutable": {
        "title": "An operation on an Immutable object (String, BigDecimal or BigInteger) won't change the object itself",
        "display_name": "UselessOperationOnImmutable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "An operation on an Immutable object (String, BigDecimal or BigInteger) won't change the object itself since the result of the operation is a new object. Therefore, ignoring the operation result is an error.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UselessOperationOnImmutable\n\n    \nimport java.math.*;\n\nclass Test {\n  void method1() {\n    BigDecimal bd=new BigDecimal(10);\n    bd.add(new BigDecimal(5)); \t\t// this will trigger the rule\n  }\n  void method2() {\n    BigDecimal bd=new BigDecimal(10);\n    bd = bd.add(new BigDecimal(5)); // this won't trigger the rule\n  }\n}\n    \n      "
    },
    "VfCsrf": {
        "title": "Avoid calling VF action upon page load",
        "display_name": "VfCsrf",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid calling VF action upon page load as the action becomes vulnerable to CSRF.\nhttps://pmd.github.io/pmd-5.8.1/pmd-visualforce/rules/vf/security.html#VfCsrfRule\n\n\t\t\t \n<apex:page controller=\"AcRestActionsController\" action=\"{!csrfInitMethod}\" >\t\n\t\t \n\t\t"
    },
    "NoHtmlComments": {
        "title": "Use JSP comments instead of HTML comments",
        "display_name": "NoHtmlComments",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In a production system, HTML comments increase the payload between the application server to the client, and serve little other purpose. Consider switching to JSP comments.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoHtmlComments\n\n\t\t\t\n<HTML><title>bad example><BODY>\n<!-- HTML comment -->\n</BODY> </HTML>\n\n<HTML><title>good example><BODY>\n<%-- JSP comment --%>\n</BODY> </HTML>\n\t\t\t\n\t\t"
    },
    "NcssTypeCount": {
        "title": "The type has an NCSS line count of {0}",
        "display_name": "NcssTypeCount",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule uses the NCSS (Non-Commenting Source Statements) algorithm to determine the number of lines of code for a given type. NCSS ignores comments, and counts actual statements. Using this algorithm, lines of code that are split are counted as one.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/codesize.html#NcssTypeCount\n\n\npublic class Foo extends Bar {\n public Foo() {\n //this class only has 6 NCSS lines\n     super();\n\n\n\n\n\n      super.foo();\n }\n}\n\n   "
    },
    "DefaultPackage": {
        "title": "Use explicit scoping instead of the default package private level",
        "display_name": "DefaultPackage",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use explicit scoping instead of accidental usage of default package private level. The rule allows methods and fields annotated with Guava's @VisibleForTesting.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#DefaultPackage\n"
    },
    "AvoidMultipleUnaryOperators": {
        "title": "Using multiple unary operators may be a bug, and/or is confusing.",
        "display_name": "AvoidMultipleUnaryOperators",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The use of multiple unary operators may be problematic, and/or confusing. Ensure that the intended usage is not a bug, or consider simplifying the expression.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#AvoidMultipleUnaryOperators\n\n            \n// These are typo bugs, or at best needlessly complex and confusing:\nint i = - -1;\nint j = + - +1;\nint z = ~~2;\nboolean b = !!true;\nboolean c = !!!true;\n\n// These are better:\nint i = 1;\nint j = -1;\nint z = 2;\nboolean b = true;\nboolean c = false;\n\n// And these just make your brain hurt:\nint i = ~-2;\nint j = -~7;\n            \n        "
    },
    "StringToString": {
        "title": "Avoid calling toString() on String objects; this is unnecessary.",
        "display_name": "StringToString",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid calling toString() on objects already known to be string instances; this is unnecessary.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#StringToString\n\n\nprivate String baz() {\n    String bar = \"howdy\";\n    return bar.toString();\n}\n\n    "
    },
    "NonStaticInitializer": {
        "title": "Non-static initializers are confusing",
        "display_name": "NonStaticInitializer",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "A non-static initializer block will be called any time a constructor is invoked (just prior to invoking the constructor). While this is a valid language construct, it is rarely used and is confusing.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#NonStaticInitializer\n\n   \npublic class MyClass {\n // this block gets run before any call to a constructor\n  {\n   System.out.println(\"I am about to construct myself\");\n  }\n}\n   \n       "
    },
    "MethodReturnsInternalArray": {
        "title": "Returning ''{0}'' may expose an internal array.",
        "display_name": "MethodReturnsInternalArray",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Exposing internal arrays to the caller violates object encapsulation since elements can be removed or replaced outside of the object that owns it. It is safer to return a copy of the array.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/sunsecure.html#MethodReturnsInternalArray\n\n  \npublic class SecureSystem {\n  UserData [] ud;\n  public UserData [] getUserData() {\n      // Don't return directly the internal array, return a copy\n      return ud;\n  }\n}\n  \n      "
    },
    "AccessorMethodGeneration": {
        "title": "Avoid autogenerated methods to access private fields and methods of inner / outer classes",
        "display_name": "AccessorMethodGeneration",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When accessing a private field / method from another class, the Java compiler will generate a accessor methods with package-private visibility. This adds overhead, and to the dex method count on Android. This situation can be avoided by changing the visibility of the field / method from private to package-private.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AccessorMethodGeneration\n\n\npublic class OuterClass {\n    private int counter;\n    /* package */ int id;\n\n    public class InnerClass {\n        InnerClass() {\n            OuterClass.this.counter++; // wrong accessor method will be generated\n        }\n\n        public int getOuterClassId() {\n            return OuterClass.this.id; // id is package-private, no accessor method needed\n        }\n    }\n}\n \n        "
    },
    "OneDeclarationPerLine": {
        "title": "Use one line for each declaration, it enhances code readability.",
        "display_name": "OneDeclarationPerLine",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Java allows the use of several variables declaration of the same type on one line. However, it can lead to quite messy code. This rule looks for several declarations on the same line.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#OneDeclarationPerLine\n\n          \nString name;            // separate declarations\nString lastname;\n\nString name, lastname;  // combined declaration, a violation\n\nString name,\n       lastname;        // combined declaration on multiple lines, no violation by default.\n                        // Set property strictMode to true to mark this as violation.\n          \n        "
    },
    "AvoidArrayLoops": {
        "title": "System.arraycopy is more efficient",
        "display_name": "AvoidArrayLoops",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Instead of manually copying data between two arrays, use the efficient System.arraycopy method instead.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#AvoidArrayLoops\n\n    \npublic class Test {\n  public void bar() {\n    int[] a = new int[10];\n    int[] b = new int[10];\n    for (int i=0;i<10;i++) {\n      b[i]=a[i];\n    }\n  }\n}\n     // this will trigger the rule\n     for (int i=0;i<10;i++) {\n       b[i]=a[c[i]];\n     }\n\n  }\n}\n    \n      "
    },
    "UseStringBufferForStringAppends": {
        "title": "Prefer StringBuffer over += for concatenating strings",
        "display_name": "UseStringBufferForStringAppends",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The use of the '+=' operator for appending strings causes the JVM to create and use an internal StringBuffer. If a non-trivial number of these concatenations are being used then the explicit use of a StringBuilder or threadsafe StringBuffer is recommended to avoid this.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/optimizations.html#UseStringBufferForStringAppends\n\n      \npublic class Foo {\n  void bar() {\n    String a;\n    a = \"foo\";\n    a += \" bar\";\n   // better would be:\n   // StringBuilder a = new StringBuilder(\"foo\");\n   // a.append(\" bar);\n  }\n}\n      \n           "
    },
    "SingularField": {
        "title": "Perhaps ''{0}'' could be replaced by a local variable.",
        "display_name": "SingularField",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Fields whose scopes are limited to just single methods do not rely on the containing object to provide them to other methods. They may be better implemented as local variables within those methods.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SingularField\n\npublic class Foo {\n    private int x;  // no reason to exist at the Foo instance level\n    public void foo(int y) {\n     x = y + 5;\n     return x;\n    }\n}\n   "
    },
    "ExcessivePackageSpecificationLength": {
        "title": "Avoid really long Package Specifications ({0} lines found).",
        "display_name": "ExcessivePackageSpecificationLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Excessive class file lengths are usually indications that the class may be burdened with excessive responsibilities that could be provided by external classes or functions. In breaking these methods apart the code becomes more managable and ripe for reuse.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#ExcessivePackageSpecificationLength\n\n\n\nCREATE OR REPLACE\nPACKAGE Foo AS\n\tPROCEDURE bar1 ;\n\tPROCEDURE bar2 ;\n        PROCEDURE bar3 ;\n\t\n    ..\n\t\n        PROCEDURE barN ;\nEND;\n   "
    },
    "AvoidCatchingThrowable": {
        "title": "A catch statement should never catch throwable since it includes errors.",
        "display_name": "AvoidCatchingThrowable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Catching Throwable errors is not recommended since its scope is very broad. It includes runtime issues such as OutOfMemoryError that should be exposed and managed separately.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidCatchingThrowable\n\n\t\npublic void bar() {\n\ttry {\n     // do something\n    } catch (Throwable th) {  // should not catch Throwable\n\t\tth.printStackTrace();\n    }\n  }\n\t\n      "
    },
    "EqualComparison": {
        "title": "Use '==='/'!==' to compare with true/false or Numbers",
        "display_name": "EqualComparison",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Using == in condition may lead to unexpected results, as the variables are automatically casted to be of the same type. The === operator avoids the casting.\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/basic.html#EqualComparison\n\n  \n// Ok\nif (someVar === true) {\n  ...\n}\n// Ok\nif (someVar !== 3) {\n  ...\n}\n// Bad\nif (someVar == true) {\n  ...\n}\n// Bad\nif (someVar != 3) {\n  ...\n}\n\n\n      "
    },
    "UnusedPrivateField": {
        "title": "Avoid unused private fields such as ''{0}''.",
        "display_name": "UnusedPrivateField",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Detects when a private field is declared and/or assigned a value, but not used.\r\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unusedcode.html#UnusedPrivateField\r\n\r\n\r\npublic class Something {\r\n  private static int FOO = 2; // Unused\r\n  private int i = 5; // Unused\r\n  private int j = 6;\r\n  public int addOne() {\r\n    return j++;\r\n  }\r\n}\r\n\r\n    "
    },
    "NoElseReturn": {
        "title": "The else block is unnecessary",
        "display_name": "NoElseReturn",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The else block in a if-else-construct is unnecessary if the `if` block contains a return. Then the content of the else block can be put outside. See also: http://eslint.org/docs/rules/no-else-return\nhttps://pmd.github.io/pmd-5.8.1/pmd-javascript/rules/ecmascript/unnecessary.html#NoElseReturn\n\n// Bad:\nif (x) {\n  return y;\n} else {\n  return z;\n}\n\n// Good:\nif (x) {\n  return y;\n}\nreturn z;\n    "
    },
    "EmptyInitializer": {
        "title": "Empty initializer was found",
        "display_name": "EmptyInitializer",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty initializers serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyInitializer\n\n   \npublic class Foo {\n\n   static {} // Why ?\n\n   {} // Again, why ?\n\n}\n    \n    "
    },
    "AvoidSynchronizedAtMethodLevel": {
        "title": "Use block level rather than method level synchronization",
        "display_name": "AvoidSynchronizedAtMethodLevel",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Method-level synchronization can cause problems when new code is added to the method. Block-level synchronization helps to ensure that only the code that needs synchronization gets it.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AvoidSynchronizedAtMethodLevel\n\n\npublic class Foo {\n  // Try to avoid this:\n  synchronized void foo() {\n  }\n  // Prefer this:\n  void bar() {\n    synchronized(this) {\n    }\n  }\n\n  // Try to avoid this for static methods:\n  static synchronized void fooStatic() {\n  }\n\n  // Prefer this:\n  static void barStatic() {\n    synchronized(Foo.class) {\n    }\n  }\n}\n\n      "
    },
    "ReturnEmptyArrayRatherThanNull": {
        "title": "Return an empty array rather than 'null'.",
        "display_name": "ReturnEmptyArrayRatherThanNull",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "For any method that returns an array, it is a better to return an empty array rather than a null reference. This removes the need for null checking all results and avoids inadvertent NullPointerExceptions.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#ReturnEmptyArrayRatherThanNull\n\npublic class Example {\n    // Not a good idea...\n    public int[] badBehavior() {\n                   // ...\n        return null;\n    }\n\n    // Good behavior\n    public String[] bonnePratique() {\n      //...\n     return new String[0];\n    }\n}\n            "
    },
    "CommentSize": {
        "title": "Comment is too large",
        "display_name": "CommentSize",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Determines whether the dimensions of non-header comments found are within the specified limits.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/comments.html#CommentSize\n\n\n/**\n*\n*\ttoo many lines!\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*/\n\n    "
    },
    "InsufficientStringBufferDeclaration": {
        "title": "StringBuffer constructor is initialized with size {0}, but has at least {1} characters appended.",
        "display_name": "InsufficientStringBufferDeclaration",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Failing to pre-size a StringBuffer or StringBuilder properly could cause it to re-size many times during runtime. This rule attempts to determine the total number the characters that are actually passed into StringBuffer.append(), but represents a best guess \"worst case\" scenario. An empty StringBuffer/StringBuilder constructor initializes the object to 16 characters. This default is assumed if the length of the constructor can not be determined.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#InsufficientStringBufferDeclaration\n\n\nStringBuffer bad = new StringBuffer();\nbad.append(\"This is a long string that will exceed the default 16 characters\");\n        \nStringBuffer good = new StringBuffer(41);\ngood.append(\"This is a long string, which is pre-sized\");\n\n    "
    },
    "MissingBreakInSwitch": {
        "title": "A switch statement does not contain a break",
        "display_name": "MissingBreakInSwitch",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Switch statements without break or return statements for each case option may indicate problematic behaviour. Empty cases are ignored as these indicate an intentional fall-through.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#MissingBreakInSwitch\n\n\npublic void bar(int status) {\n    switch(status) {\n      case CANCELLED:\n        doCancelled();\n        // break; hm, should this be commented out?\n      case NEW:\n        doNew();\n        // is this really a fall-through?\n      case REMOVED:\n        doRemoved();\n        // what happens if you add another case after this one?\n      case OTHER: // empty case - this is interpreted as an intentional fall-through\n      case ERROR:\n        doErrorHandling();\n        break;\n    }\n}\n\n      "
    },
    "UnnecessaryFinalModifier": {
        "title": "Unnecessary final modifier in final class / private methods",
        "display_name": "UnnecessaryFinalModifier",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "When a class has the final modifier, all the methods are automatically final and do not need to be tagged as such. Similarly, private methods can't be overriden, and therefore do not need to be tagged either.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UnnecessaryFinalModifier\n\n\npublic final class Foo {\n    // This final modifier is not necessary, since the class is final\n    // and thus, all methods are final\n    private final void foo() {\n    }\n}\n\n\n      "
    },
    "MistypedCDATASection": {
        "title": "Potentialy mistyped CDATA section with extra [ at beginning or ] at the end.",
        "display_name": "MistypedCDATASection",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "An XML CDATA section begins with a <!CDATA[ marker, which has only one [, and ends with a ]]> marker, which has only two ].\nhttps://pmd.github.io/pmd-5.8.1/pmd-xml/rules/xml/basic.html#MistypedCDATASection\n\n \nAn extra [ looks like &lt;!CDATA[[]]&gt;, and an extra ] looks like &lt;!CDATA[]]]&gt;.\n \n     "
    },
    "AvoidDollarSigns": {
        "title": "Avoid using dollar signs in variable/method/class/interface names",
        "display_name": "AvoidDollarSigns",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using dollar signs in variable/method/class/interface names.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#AvoidDollarSigns\n\n   \npublic class Fo$o {  // not a recommended name\n}\n   \n       "
    },
    "MisplacedNullCheck": {
        "title": "The null check here is misplaced; if the variable is null there will be a NullPointerException",
        "display_name": "MisplacedNullCheck",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The null check here is misplaced. If the variable is null a NullPointerException will be thrown. Either the check is useless (the variable will never be \"null\") or it is incorrect.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#MisplacedNullCheck\n\n    \npublic class Foo {\n\tvoid bar() {\n\t\tif (a.equals(baz) && a != null) {}\n\t\t}\n}\n    \n      "
    },
    "AvoidFinalLocalVariable": {
        "title": "Avoid using final local variables, turn them into fields",
        "display_name": "AvoidFinalLocalVariable",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using final local variables, turn them into fields.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidFinalLocalVariable\n\npublic class MyClass {\n    public void foo() {\n        final String finalLocalVariable;\n    }\n}\n       "
    },
    "ExcessiveParameterList": {
        "title": "Avoid long parameter lists.",
        "display_name": "ExcessiveParameterList",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Methods with numerous parameters are a challenge to maintain, especially if most of them share the same datatype. These situations usually denote the need for new objects to wrap the numerous parameters.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#ExcessiveParameterList\n\n\nCREATE OR REPLACE\nPROCEDURE addPerson(\t\t-- too many arguments liable to be mixed up\n\tbirthYear pls_integer, birthMonth pls_integer, birthDate pls_integer, height pls_integer, weight pls_integer, ssn pls_integer) {\n\n\t. . . .\nEND ADDPERSON;\n \nCREATE OR REPLACE\nPROCEDURE addPerson(\t\t-- preferred approach\n\tbirthdate DATE, measurements BodyMeasurements , ssn INTEGER) BEGIN\n\n\t. . . .\nEND;\n\n   "
    },
    "AbstractClassWithoutAbstractMethod": {
        "title": "This abstract class does not have any abstract methods",
        "display_name": "AbstractClassWithoutAbstractMethod",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The abstract class does not contain any abstract methods. An abstract class suggests an incomplete implementation, which is to be completed by subclasses implementing the abstract methods. If the class is intended to be used as a base class only (not to be instantiated directly) a protected constructor can be provided prevent direct instantiation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#AbstractClassWithoutAbstractMethod\n\n\npublic abstract class Foo {\n  void int method1() { ... }\n  void int method2() { ... }\n  // consider using abstract methods or removing\n  // the abstract modifier and adding protected constructors\n}\n\n      "
    },
    "LawOfDemeter": {
        "title": "Potential violation of Law of Demeter",
        "display_name": "LawOfDemeter",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The Law of Demeter is a simple rule, that says \"only talk to friends\". It helps to reduce coupling between classes or objects. See also the references: Andrew Hunt, David Thomas, and Ward Cunningham. The Pragmatic Programmer. From Journeyman to Master. Addison-Wesley Longman, Amsterdam, October 1999.; K.J. Lieberherr and I.M. Holland. Assuring good style for object-oriented programs. Software, IEEE, 6(5):38\u201348, 1989.; http://www.ccs.neu.edu/home/lieber/LoD.html; http://en.wikipedia.org/wiki/Law_of_Demeter\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/coupling.html#LawOfDemeter\n\n\npublic class Foo {\n    /**\n     * This example will result in two violations.\n     */\n    public void example(Bar b) {\n        // this method call is ok, as b is a parameter of \"example\"\n        C c = b.getC();\n        \n        // this method call is a violation, as we are using c, which we got from B.\n        // We should ask b directly instead, e.g. \"b.doItOnC();\"\n        c.doIt();\n        \n        // this is also a violation, just expressed differently as a method chain without temporary variables.\n        b.getC().doIt();\n        \n        // a constructor call, not a method call.\n        D d = new D();\n        // this method call is ok, because we have create the new instance of D locally.\n        d.doSomethingElse(); \n    }\n}\n\n        "
    },
    "CloneThrowsCloneNotSupportedException": {
        "title": "clone() method should throw CloneNotSupportedException",
        "display_name": "CloneThrowsCloneNotSupportedException",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The method clone() should throw a CloneNotSupportedException.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/clone.html#CloneThrowsCloneNotSupportedException\n\n             \n public class MyClass implements Cloneable{\n     public Object clone() { // will cause an error\n          MyClass clone = (MyClass)super.clone();\n          return clone;\n     }\n }\n    \n         "
    },
    "SimplifyBooleanAssertion": {
        "title": "assertTrue(!expr) can be replaced by assertFalse(expr)",
        "display_name": "SimplifyBooleanAssertion",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid negation in an assertTrue or assertFalse test. For example, rephrase: assertTrue(!expr); as: assertFalse(expr);\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#SimplifyBooleanAssertion\n\n\npublic class SimpleTest extends TestCase {\n   public void testX() {\n     assertTrue(\"not empty\", !r.isEmpty()); // replace with assertFalse(\"not empty\", r.isEmpty())\n     assertFalse(!r.isEmpty()); // replace with assertTrue(r.isEmpty())\n   }\n}\n\n          "
    },
    "ExcessivePackageBodyLength": {
        "title": "Avoid really long Object Type and Package bodies ({0} lines found).",
        "display_name": "ExcessivePackageBodyLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Excessive class file lengths are usually indications that the class may be burdened with excessive responsibilities that could be provided by external classes or functions. In breaking these methods apart the code becomes more managable and ripe for reuse.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#ExcessivePackageBodyLength\n\n\nCREATE OR REPLACE\nPACKAGE BODY Foo AS\n\tPROCEDURE bar1 IS BEGIN\n    -- 1000 lines of code\n\tEND bar1;\n\tPROCEDURE bar2 IS BEGIN\n    -- 1000 lines of code\n\tEND bar2;\n    PROCEDURE bar3 IS BEGIN\n    -- 1000 lines of code\n\tEND bar3;\n\t\n\t\n    PROCEDURE barN IS BEGIN\n    -- 1000 lines of code\n\tEND barn;\nEND;\n\n   "
    },
    "ForLoopShouldBeWhileLoop": {
        "title": "This for loop could be simplified to a while loop",
        "display_name": "ForLoopShouldBeWhileLoop",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Some for loops can be simplified to while loops, this makes them more concise.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#ForLoopShouldBeWhileLoop\n\n  \npublic class Foo {\n\tvoid bar() {\n\t\tfor (;true;) true; // No Init or Update part, may as well be: while (true)\n\t}\n}\n \n      "
    },
    "AvoidSoqlInLoops": {
        "title": "Avoid Soql queries inside loops",
        "display_name": "AvoidSoqlInLoops",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "New objects created within loops should be checked to see if they can created outside them and reused.\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/performance.html#AvoidSoqlInLoops\n\npublic class Something {\n\tpublic static void main( String as[] ) {  \n\t\tfor (Integer i = 0; i < 10; i++) {\n\t\t\tList<Account> accounts = [SELECT Id FROM Account];\n\t\t}\n\t}\n}\n\n    "
    },
    "UnusedFormalParameter": {
        "title": "Avoid unused {0} parameters such as ''{1}''.",
        "display_name": "UnusedFormalParameter",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid passing parameters to methods or constructors without actually referencing them in the method body.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unusedcode.html#UnusedFormalParameter\n\n\npublic class Foo {\n\tprivate void bar(String howdy) {\n\t// howdy is not used\n\t}\n}\n\n    "
    },
    "AvoidUsingNativeCode": {
        "title": "The use of native code is not recommended.",
        "display_name": "AvoidUsingNativeCode",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Unnecessary reliance on Java Native Interface (JNI) calls directly reduces application portability and increases the maintenance burden.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidUsingNativeCode\n\n            \npublic class SomeJNIClass {\n\n     public SomeJNIClass() {\n         System.loadLibrary(\"nativelib\");\n     }\n\n     static {\n         System.loadLibrary(\"nativelib\");\n         }\n\n     public void invalidCallsInMethod() throws SecurityException, NoSuchMethodException {\n         System.loadLibrary(\"nativelib\");\n     }\n}\n            \n        "
    },
    "SimplifyBooleanExpressions": {
        "title": "Avoid unnecessary comparisons in boolean expressions",
        "display_name": "SimplifyBooleanExpressions",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid unnecessary comparisons in boolean expressions, they serve no purpose and impacts readability.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#SimplifyBooleanExpressions\n\n  \npublic class Bar {\n  // can be simplified to\n  // bar = isFoo();\n  private boolean bar = (isFoo() == true);\n\n  public isFoo() { return false;}\n}\n  \n      "
    },
    "IdempotentOperations": {
        "title": "Avoid idempotent operations (like assigning a variable to itself).",
        "display_name": "IdempotentOperations",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid idempotent operations - they have no effect.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#IdempotentOperations\n\n      \npublic class Foo {\n public void bar() {\n  int x = 2;\n  x = x;\n }\n}\n      \n      "
    },
    "EmptyMethodInAbstractClassShouldBeAbstract": {
        "title": "An empty method in an abstract class should be abstract instead",
        "display_name": "EmptyMethodInAbstractClassShouldBeAbstract",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty or auto-generated methods in an abstract class should be tagged as abstract. This helps to remove their inapproprate usage by developers who should be implementing their own versions in the concrete subclasses.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#EmptyMethodInAbstractClassShouldBeAbstract\n\n        \t\npublic abstract class ShouldBeAbstract {\n    public Object couldBeAbstract() {\n        // Should be abstract method ?\n        return null;\n    }\n\n    public void couldBeAbstract() {\n    }\n}\n\t     \t\n    \t"
    },
    "AvoidAccessibilityAlteration": {
        "title": "You should modify visibility of class or methods using getDeclaredConstructors(), getDeclaredConstructor(Class[]), setAccessible() or PrivilegedAction.",
        "display_name": "AvoidAccessibilityAlteration",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Methods such as getDeclaredConstructors(), getDeclaredConstructor(Class[]) and setAccessible(), as the interface PrivilegedAction, allows for the runtime alteration of variable, class, or method visibility, even if they are private. This violates the principle of encapsulation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#AvoidAccessibilityAlteration\n\n            \n\nimport java.lang.reflect.AccessibleObject;\nimport java.lang.reflect.Method;\nimport java.security.PrivilegedAction;\n\npublic class Violation {\n  public void invalidCallsInMethod() throws SecurityException, NoSuchMethodException {\n    // Possible call to forbidden getDeclaredConstructors\n    Class[] arrayOfClass = new Class[1];\n    this.getClass().getDeclaredConstructors();\n    this.getClass().getDeclaredConstructor(arrayOfClass);\n    Class clazz = this.getClass();\n    clazz.getDeclaredConstructor(arrayOfClass);\n    clazz.getDeclaredConstructors();\n      // Possible call to forbidden setAccessible\n    clazz.getMethod(\"\", arrayOfClass).setAccessible(false);\n    AccessibleObject.setAccessible(null, false);\n    Method.setAccessible(null, false);\n    Method[] methodsArray = clazz.getMethods();\n    int nbMethod;\n    for ( nbMethod = 0; nbMethod < methodsArray.length; nbMethod++ ) {\n      methodsArray[nbMethod].setAccessible(false);\n    }\n\n      // Possible call to forbidden PrivilegedAction\n    PrivilegedAction priv = (PrivilegedAction) new Object(); priv.run();\n  }\n}\n          \n      "
    },
    "BooleanGetMethodName": {
        "title": "A 'getX()' method which returns a boolean should be named 'isX()'",
        "display_name": "BooleanGetMethodName",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Methods that return boolean results should be named as predicate statements to denote this. I.e, 'isReady()', 'hasValues()', 'canCommit()', 'willFail()', etc. Avoid the use of the 'get' prefix for these methods.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/naming.html#BooleanGetMethodName\n\n            \npublic boolean getFoo(); \t// bad\npublic boolean isFoo(); \t// ok\npublic boolean getFoo(boolean bar); // ok, unless checkParameterizedMethods=true\n     "
    },
    "EmptyStatementBlock": {
        "title": "Avoid empty block statements.",
        "display_name": "EmptyStatementBlock",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Empty block statements serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyStatementBlock\n\n    \npublic class Foo {\n\n   private int _bar;\n\n   public void setBar(int bar) {\n      { _bar = bar; } // Why not?\n      {} // But remove this.\n   }\n\n}\n    \n    "
    },
    "InefficientStringBuffering": {
        "title": "Avoid concatenating nonliterals in a StringBuffer/StringBuilder constructor or append().",
        "display_name": "InefficientStringBuffering",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid concatenating non-literals in a StringBuffer constructor or append() since intermediate buffers will need to be be created and destroyed by the JVM.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strings.html#InefficientStringBuffering\n\n\n    // Avoid this, two buffers are actually being created here\nStringBuffer sb = new StringBuffer(\"tmp = \"+System.getProperty(\"java.io.tmpdir\"));\n    \n    // do this instead\nStringBuffer sb = new StringBuffer(\"tmp = \");\nsb.append(System.getProperty(\"java.io.tmpdir\"));\n\n    "
    },
    "UselessQualifiedThis": {
        "title": "Useless qualified this usage in the same class.",
        "display_name": "UselessQualifiedThis",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Look for qualified this usages in the same class.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/unnecessary.html#UselessQualifiedThis\n\n    \npublic class Foo {\n    final Foo otherFoo = Foo.this;  // use \"this\" directly\n\n    public void doSomething() {\n         final Foo anotherFoo = Foo.this;  // use \"this\" directly\n    }\n\n    private ActionListener returnListener() {\n        return new ActionListener() {\n            @Override\n            public void actionPerformed(ActionEvent e) {\n                doSomethingWithQualifiedThis(Foo.this);  // This is fine\n            }\n        };\n    }\n\n    private class Foo3 {\n        final Foo myFoo = Foo.this;  // This is fine\n    }\n\n    private class Foo2 {\n        final Foo2 myFoo2 = Foo2.this;  // Use \"this\" direclty\n    }\n}\n    \n    "
    },
    "AvoidLogicInTrigger": {
        "title": "Avoid logic in triggers",
        "display_name": "AvoidLogicInTrigger",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "As triggers do not allow methods like regular classes they are less flexible and suited to apply good encapsulation style. Therefore delegate the triggers work to a regular class (often called Trigger handler class). See more here: https://developer.salesforce.com/page/Trigger_Frameworks_and_Apex_Trigger_Best_Practices\nhttps://pmd.github.io/pmd-5.8.1/pmd-apex/rules/apex/style.html#AvoidLogicInTrigger\n\ntrigger Accounts on Account (before insert, before update, before delete, after insert, after update, after delete, after undelete) {\n\tfor(Account acc : Trigger.new) {           \n\t\tif(Trigger.isInsert) {\n\t\t\t...\n\t\t}\n\t\t\n\t\t...\n\t\t\n\t\tif(Trigger.isDelete) {\n\t\t\t...\n\t\t}\n\t}\n}\n\n    "
    },
    "SimplifiedTernary": {
        "title": "Ternary operators that can be simplified with || or &&",
        "display_name": "SimplifiedTernary",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Look for ternary operators with the form `condition ? literalBoolean : foo` or `condition ? foo : literalBoolean`. These expressions can be simplified respectively to `condition || foo` when the literalBoolean is true `!condition && foo` when the literalBoolean is false or `!condition || foo` when the literalBoolean is true `condition && foo` when the literalBoolean is false\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/basic.html#SimplifiedTernary\n\n        \npublic class Foo {\n    public boolean test() {\n        return condition ? true : something(); // can be as simple as return condition || something();\n    }\n\n    public void test2() {\n        final boolean value = condition ? false : something(); // can be as simple as value = !condition && something();\n    }\n\n    public boolean test3() {\n        return condition ? something() : true; // can be as simple as return !condition || something();\n    }\n\n    public void test4() {\n        final boolean otherValue = condition ? something() : false; // can be as simple as condition && something();\n    }\n}\n        \n    "
    },
    "NcssMethodCount": {
        "title": "The method {0}() has an NCSS line count of {1}",
        "display_name": "NcssMethodCount",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule uses the NCSS (Non-Commenting Source Statements) algorithm to determine the number of lines of code for a given method. NCSS ignores comments, and counts actual statements. Using this algorithm, lines of code that are split are counted as one.\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/codesize.html#NcssMethodCount\n\n\nCREATE OR REPLACE PACKAGE BODY AS\n FUNCTION methd RETURN INTEGER IS\n BEGIN\n   RETURN 1;;\n END;\nEND;\n\n   "
    },
    "NoInlineScript": {
        "title": "Avoiding inlining HTML script content",
        "display_name": "NoInlineScript",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid inlining HTML script content. Consider externalizing the HTML script using the 'src' attribute on the \"script\" element. Externalized script could be reused between pages. Browsers can also cache the script, reducing overall download bandwidth.\nhttps://pmd.github.io/pmd-5.8.1/pmd-jsp/rules/jsp/basic.html#NoInlineScript\n\n            \n                Most browsers should be able to interpret the following headers:\n                \n                <%@ page contentType=\"text/html; charset=UTF-8\" pageEncoding=\"UTF-8\" %>\n                    \n                <meta http-equiv=\"Content-Type\"  content=\"text/html; charset=UTF-8\" />\n            \n        "
    },
    "FieldDeclarationsShouldBeAtStartOfClass": {
        "title": "Fields should be declared at the top of the class, before any method declarations, constructors, initializers or inner classes.",
        "display_name": "FieldDeclarationsShouldBeAtStartOfClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Fields should be declared at the top of the class, before any method declarations, constructors, initializers or inner classes.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#FieldDeclarationsShouldBeAtStartOfClass\n\n      \npublic class HelloWorldBean {\n\n  // Field declared before methods / inner classes - OK\n  private String _thing;\n\n  public String getMessage() {\n    return \"Hello World!\";\n  }\n\n  // Field declared after methods / inner classes - avoid this\n  private String _fieldInWrongLocation;\n}\n      \n    "
    },
    "UseUtilityClass": {
        "title": "All methods are static.  Consider using a utility class instead. Alternatively, you could add a private constructor or make the class abstract to silence this warning.",
        "display_name": "UseUtilityClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "For classes that only have static methods, consider making them utility classes. Note that this doesn't apply to abstract classes, since their subclasses may well include non-static methods. Also, if you want this class to be a utility class, remember to add a private constructor to prevent instantiation. (Note, that this use was known before PMD 5.1.0 as UseSingleton).\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#UseUtilityClass\n\n\npublic class MaybeAUtility {\n  public static void foo() {}\n  public static void bar() {}\n}\n\n    "
    },
    "UseAssertNullInsteadOfAssertTrue": {
        "title": "Use assertNull(x) instead of assertTrue(x==null), or assertNotNull(x) vs assertFalse(x==null)",
        "display_name": "UseAssertNullInsteadOfAssertTrue",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "This rule detects JUnit assertions in object references equality. These assertions should be made by more specific methods, like assertNull, assertNotNull.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/junit.html#UseAssertNullInsteadOfAssertTrue\n\n \n public class FooTest extends TestCase {\n  void testCode() {\n   Object a = doSomething();\n   assertTrue(a==null); // bad usage\n   assertNull(a);  // good usage\n   assertTrue(a != null); // bad usage\n   assertNotNull(a);  // good usage\n  }\n }\n \n       "
    },
    "AvoidCatchingGenericException": {
        "title": "Avoid catching generic exceptions such as NullPointerException, RuntimeException, Exception in try-catch block",
        "display_name": "AvoidCatchingGenericException",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid catching generic exceptions such as NullPointerException, RuntimeException, Exception in try-catch block\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/strictexception.html#AvoidCatchingGenericException\n\n    \npackage com.igate.primitive;\n    \npublic class PrimitiveType {\n    \n  public void downCastPrimitiveType() {\n    try {\n      System.out.println(\" i [\" + i + \"]\");\n    } catch(Exception e) {\n      e.printStackTrace();\n    } catch(RuntimeException e) {\n      e.printStackTrace();\n    } catch(NullPointerException e) {\n      e.printStackTrace();\n    }\n  } \n}\n    \n    "
    },
    "JUnit4SuitesShouldUseSuiteAnnotation": {
        "title": "JUnit 4 indicates test suites via annotations, not the suite method.",
        "display_name": "JUnit4SuitesShouldUseSuiteAnnotation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "In JUnit 3, test suites are indicated by the suite() method. In JUnit 4, suites are indicated through the @RunWith(Suite.class) annotation.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#JUnit4SuitesShouldUseSuiteAnnotation\n\n\npublic class BadExample extends TestCase{\n\n    public static Test suite(){\n    \treturn new Suite();\n    }\n}\n\n@RunWith(Suite.class)\n@SuiteClasses( { TestOne.class, TestTwo.class })\npublic class GoodTest {\n}\n      "
    },
    "OptimizableToArrayCall": {
        "title": "This call to Collection.toArray() may be optimizable",
        "display_name": "OptimizableToArrayCall",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calls to a collection's toArray() method should specify target arrays sized to match the size of the collection. Initial arrays that are too small are discarded in favour of new ones that have to be created that are the proper size.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#OptimizableToArrayCall\n\n  \nList foos = getFoos();\n\n    // inefficient, the array will be discarded\nFoo[] fooArray = foos.toArray(new Foo[0]);\n\n    // much better; this one sizes the destination array,\n    // avoiding of a new one via reflection\nFoo[] fooArray = foos.toArray(new Foo[foos.size()]);\n  \n      "
    },
    "ExcessiveTemplateLength": {
        "title": "Template is too long",
        "display_name": "ExcessiveTemplateLength",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The template is too long. It should be broken up into smaller pieces.\nhttps://pmd.github.io/pmd-5.8.1/pmd-vm/rules/vm/basic.html#ExcessiveTemplateLength\n"
    },
    "NullAssignment": {
        "title": "Assigning an Object to null is a code smell.  Consider refactoring.",
        "display_name": "NullAssignment",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Assigning a \"null\" to a variable (outside of its declaration) is usually bad form. Sometimes, this type of assignment is an indication that the programmer doesn't completely understand what is going on in the code. NOTE: This sort of assignment may used in some cases to dereference objects and encourage garbage collection.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#NullAssignment\n\n \npublic void bar() {\n  Object x = null; // this is OK\n  x = new Object();\n     // big, complex piece of code here\n  x = null; // this is not required\n     // big, complex piece of code here\n}\n\n \n      "
    },
    "MisplacedPragma": {
        "title": "Pragma should be used only inside the declaration block before 'BEGIN'.",
        "display_name": "MisplacedPragma",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Oracle states that the PRAQMA AUTONOMOUS_TRANSACTION must be in the declaration block, but the code does not complain, when being compiled on the 11g DB. https://docs.oracle.com/cd/B28359_01/appdev.111/b28370/static.htm#BABIIHBJ\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/strictsyntax.html#MisplacedPragma\n\ncreate or replace package inline_pragma_error is\n\nend;\n/\n\ncreate or replace package body inline_pragma_error is\n  procedure do_transaction(p_input_token        in varchar(200)) is\n  PRAGMA AUTONOMOUS_TRANSACTION; /* this is correct place for PRAGMA */\n  begin\n    PRAGMA AUTONOMOUS_TRANSACTION; /* this is the wrong place for PRAGMA -> violation */\n    /* do something */\n    COMMIT;\n   end do_transaction;\n\nend inline_pragma_error;\n/\n\n    "
    },
    "TO_TIMESTAMPWithoutDateFormat": {
        "title": "TO_TIMESTAMP without date format",
        "display_name": "TO_TIMESTAMPWithoutDateFormat",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "TO_TIMESTAMP without date format- use TO_TIMESTAMP(expression, date-format)\nhttps://pmd.github.io/pmd-5.8.1/pmd-plsql/rules/plsql/dates.html#TO_TIMESTAMPWithoutDateFormat\n\n\nCREATE OR REPLACE PACKAGE BODY date_utilities\nIS\n \n-- Take single parameter, relyimg on current default NLS date format \nFUNCTION to_timestamp_single_parameter (p_date_string IN VARCHAR2) RETURN DATE\nIS\nBEGIN\n   RETURN TO_TIMESTAMP(p_date_string); \nEND to_timestamp_single_parameter ;\n\n-- Take 2 parameters, using an explicit date format string  \nFUNCTION to_timestamp_two_parameters (p_date_string IN VARCHAR2, p_format_mask IN VARCHAR2) RETURN DATE\nIS\nBEGIN\n   TO_TIMESTAMP(p_date_string, p_date_format); \nEND to_timestamp_two_parameters ;\n\n-- Take 3 parameters, using an explicit date format string and an explicit language    \nFUNCTION to_timestamp_three_parameters (p_date_string IN VARCHAR2, p_format_mask IN VARCHAR2, p_nls_language VARCHAR2 ) RETURN DATE\nIS\nBEGIN\n   TO_TIMESTAMP(p_date_string, p_format_mask, p_nls_language); \nEND to_timestamp_three_parameters ;\n\nEND date_utilities ;\n/\n\n  "
    },
    "EmptyStaticInitializer": {
        "title": "Empty static initializer was found",
        "display_name": "EmptyStaticInitializer",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "An empty static initializer serve no purpose and should be removed.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/empty.html#EmptyStaticInitializer\n\n   \npublic class Foo {\n\tstatic {\n\t// empty\n\t}\n}\n\n       "
    },
    "AvoidAssertAsIdentifier": {
        "title": "Avoid using assert as an identifier; it became a reserved word in JDK 1.4",
        "display_name": "AvoidAssertAsIdentifier",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use of the term 'assert' will conflict with newer versions of Java since it is a reserved word.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#AvoidAssertAsIdentifier\n\n  \npublic class A {\n\tpublic  class foo {\n\t\tString assert = \"foo\";\n\t}\n}\n  \n      "
    },
    "TooFewBranchesForASwitchStatement": {
        "title": "A switch with less than three branches is inefficient, use a 'if statement' instead.",
        "display_name": "TooFewBranchesForASwitchStatement",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Switch statements are indended to be used to support complex branching behaviour. Using a switch for only a few cases is ill-advised, since switches are not as easy to understand as if-then statements. In these cases use the if-then statement to increase code readability.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#TooFewBranchesForASwitchStatement\n\n            \n// With a minimumNumberCaseForASwitch of 3\npublic class Foo {\n    public void bar() {\n        switch (condition) {\n            case ONE:\n                instruction;\n                break;\n            default:\n                break; // not enough for a 'switch' stmt, a simple 'if' stmt would have been more appropriate\n        }\n    }\n}\n            \n        "
    },
    "UnnecessaryParentheses": {
        "title": "This statement may have some unnecessary parentheses",
        "display_name": "UnnecessaryParentheses",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Sometimes expressions are wrapped in unnecessary parentheses, making them look like function calls.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/controversial.html#UnnecessaryParentheses\n\n  \npublic class Foo {\n   boolean bar() {\n      return (true);\n      }\n}\n  \n      "
    },
    "ArrayIsStoredDirectly": {
        "title": "The user-supplied array ''{0}'' is stored directly.",
        "display_name": "ArrayIsStoredDirectly",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Constructors and methods receiving arrays should clone objects and store the copy. This prevents future changes from the user from affecting the original array.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/sunsecure.html#ArrayIsStoredDirectly\n\n  \npublic class Foo {\n  private String [] x;\n    public void foo (String [] param) {\n      // Don't do this, make a copy of the array at least\n      this.x=param;\n    }\n}\n  \n      "
    },
    "LooseCoupling": {
        "title": "Avoid using implementation types like ''{0}''; use the interface instead",
        "display_name": "LooseCoupling",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Avoid using implementation types (i.e., HashSet); use the interface (i.e, Set) instead\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/typeresolution.html#LooseCoupling\n\n\nimport java.util.ArrayList;\nimport java.util.HashSet;\n\npublic class Bar {\n\t\t// Use List instead\n\tprivate ArrayList list = new ArrayList();\n\t\t// Use Set instead\n\tpublic HashSet getFoo() {\n    return new HashSet();\n  }\n}\n  \n      "
    },
    "IntegerInstantiation": {
        "title": "Avoid instantiating Integer objects. Call Integer.valueOf() instead.",
        "display_name": "IntegerInstantiation",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Calling new Integer() causes memory allocation that can be avoided by the static Integer.valueOf(). It makes use of an internal cache that recycles earlier instances making it more memory efficient.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#IntegerInstantiation\n\n  \npublic class Foo {\n\tprivate Integer i = new Integer(0); // change to Integer i = Integer.valueOf(0);\n}\n   \n      "
    },
    "GodClass": {
        "title": "Possible God class",
        "display_name": "GodClass",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "The God Class rule detects the God Class design flaw using metrics. God classes do too many things, are very big and overly complex. They should be split apart to be more object-oriented. The rule uses the detection strategy described in \"Object-Oriented Metrics in Practice\". The violations are reported against the entire class. See also the references: Michele Lanza and Radu Marinescu. Object-Oriented Metrics in Practice: Using Software Metrics to Characterize, Evaluate, and Improve the Design of Object-Oriented Systems. Springer, Berlin, 1 edition, October 2006. Page 80.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/design.html#GodClass\n"
    },
    "AvoidEnumAsIdentifier": {
        "title": "Avoid using enum as an identifier; it's a reserved word in JDK 1.5",
        "display_name": "AvoidEnumAsIdentifier",
        "severity": "1",
        "categories": [
            "security"
        ],
        "description": "Use of the term 'enum' will conflict with newer versions of Java since it is a reserved word.\nhttps://pmd.github.io/pmd-5.8.1/pmd-java/rules/java/migrating.html#AvoidEnumAsIdentifier\n\n  \npublic class A {\n\tpublic  class foo {\n\t\tString enum = \"foo\";\n\t}\n}\n  \n      "
    }
}
