package main

import (
	"fmt"
	"net/http"
	"text/template"
)

type Data struct {
	Error string
	URLS  []string
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/style.css", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, "./static/style.css")
	})

	port := os.Getenv("PORT")
	fmt.Println("Now listening on " + port)
	http.ListenAndServe(":" + port, nil)
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	t, e := template.ParseFiles("views/index.html")
	if e != nil {
		fmt.Println(e)
	}

	var data Data

	if r.Method == "POST" {
		r.ParseForm()

		longURL := r.PostForm["url"][0]
		data.URLS = append(data.URLS, longURL)

		resp, err := http.Get(longURL)
		if err == nil {
			defer resp.Body.Close()
			if resp.StatusCode == 200 {
				data.URLS = append(data.URLS, resp.Request.URL.String())
			} else {
				data.Error = "The request failed"
			}
		} else {
			data.Error = "Invalid URL"
		}
	}

	t.Execute(w, data)
}
