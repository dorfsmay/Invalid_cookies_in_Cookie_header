package main

import (
	"fmt"
	"log"
	"net/http"
)

func cookies(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Cookies())
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK!"))
}

func main() {
	http.HandleFunc("/", cookies)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
