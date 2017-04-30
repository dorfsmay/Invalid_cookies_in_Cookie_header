package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func cookies(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Cookies())
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK!"))
}

func main() {
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", cookies).Methods("GET")
	log.Fatal(http.ListenAndServe(":8080", router))
}
