'''
This is my sample Kotlin file. It contains all of the core concepts in software development
and serves as a template and reference for future projects.

eutoApps, May 2024
'''

import java.io.File
import java.io.IOException

// Define a class representing a Person with a name and age
//Amy and Bob will be instantiations of Person done in main() below
class Person(val name: String, var age: Int) {
    // Method to make the Person speak
    fun speak() {
        println("Hello, my name is $name and I'm $age years old.")
    }
}

// Define an interface for Animals =======================================================================
interface Animal {
    // Method to make an Animal produce a sound
    fun makeSound()
}

// Implement the Animal interface for a Dog
class Dog : Animal {
    override fun makeSound() {
        println("Arf!")
    }
}

fun main() {
    // Variables declaration
    val message: String = "Hello, Kotlin!" // Immutable variable (val) with explicit type declaration
    var count: Int = 10 // Mutable variable (var) with explicit type declaration

    println(message)

    // Conditional statements (if-else)
    if (count > 5) {
        println("Count is greater than 5")
    } else {
        println("Count is less than or equal to 5")
    }

    // Loop (for loop)
    for (i in 1..10) {
        println("Count: $i")
    }

    // Create objects of type Person =======================================================================
    val person1 = Person("Alice", 30)
    val person2 = Person("Bob", 25)

    person1.speak() // Call the speak method of person1
    person2.speak() // Call the speak method of person2


    // Collections (listOf creates an immutable List)
    val numbers = listOf(1, 2, 3, 4, 5)
    println("Numbers: $numbers")

    // Exception handling (try-catch block)
    val x = 10
    val y = 0
    try {
        val result = x / y
        println("Result: $result")
    } catch (e: ArithmeticException) {
        println("Error: ${e.message}")
    }

    // File I/O (writing to a file) ========================================================================
    val fileName = "sample.txt"
    val fileContent = "This is a sample file content."
    try {
        File(fileName).writeText(fileContent) // Write content to a file
        println("File '$fileName' created successfully.")
    } catch (e: IOException) {
        println("Error writing to file: ${e.message}")
    }

    // File I/O (reading from a file)
    try {
        val content = File(fileName).readText() // Read content from a file
        println("File content: $content")
    } catch (e: IOException) {
        println("Error reading from file: ${e.message}")
    }

    // Anonymous function (lambda expression) ===============================================================
    val doubleValue = { z: Int -> z * 2 } // Doubling function using lambda expression
    println("Double of 5: ${doubleValue(5)}")

    // Lambda expression (function literal)
    val square: (Int) -> Int = { it * it } // Square function using lambda expression
    println("Square of 4: ${square(4)}")

    // Higher-order function
    fun operateOnNumber(x: Int, operation: (Int) -> Int): Int {
        return operation(x)
    }

    val result1 = operateOnNumber(5) { it * 2 } // Pass a lambda expression directly
    println("Result1: $result1")

    val result2 = operateOnNumber(10, square) // Pass a lambda function as a parameter
    println("Result2: $result2")

    // Extension function (extends existing Int type with isEven method) ========================================
    fun Int.isEven(): Boolean {
        return this % 2 == 0
    }

    println("Is 6 even? ${6.isEven()}")
    println("Is 7 even? ${7.isEven()}")

    // Nullable types and Elvis operator
    var nullableString: String? = null // Declare a nullable String
    println(nullableString?.length) // Safe call operator returns null because nullableString is null

    val nonNullString: String = nullableString ?: "Default Value" // Elvis operator returns a default value if nullableString is null
    println(nonNullString)


    // Smart casts (using "is" operator)
    val obj: Any = "Hello"
    if (obj is String) {
        println("Length: ${obj.length}") // Smart cast to String, so length property is accessible
    }

    // Ranges =====================================================================================================
    val range = 1..10 // Inclusive range from 1 to 10
    println("Range: $range")

    // When expression (replacement for switch statement)
    val number = 5
    val result = when (number) {
        in 1..3 -> "Small number"
        in 4..7 -> "Medium number"
        else -> "Large number"
    }
    println("Result: $result")

    // Using "when" with type check
    val animal: Animal = Dog()
    when (animal) {
        is Dog -> animal.makeSound()
    }
}
