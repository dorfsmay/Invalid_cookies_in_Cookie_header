package main

import "fmt"
import "net/http"

func cookies(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Cookies())
}

func main() {
	http.HandleFunc("/", cookies)
	http.ListenAndServe(":8080", nil)
}
