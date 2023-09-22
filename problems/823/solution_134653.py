import "fmt"
 
func main() {
  var n, tmp int
  cnt := 0
 
  fmt.Scanln(&n)
 
  for i := 1; i < n; i++ {
    fmt.Scanln(&tmp)
    cnt += tmp
  } 
 
  fmt.Println(n*(1+n)/2 - cnt)
}