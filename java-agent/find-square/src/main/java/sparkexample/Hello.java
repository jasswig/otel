package sparkexample;

import static spark.Spark.*;

public class Hello {

    public static void main(String[] args) {
        get("/", (req, res) -> {
            return "hello from sparkjava.com";
        });
    }

}