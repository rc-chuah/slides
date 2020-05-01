package main

import "testing"

func TestAdd(t *testing.T) {
	t.Log("Hello from the test")
	total := add(2, 2)
	if total != 4 {
		t.Error("Sum was incorrect")
	}
}

func TestAddAgain(t *testing.T) {
	t.Log("Hello from the test")
	total := add(3, 3)
	if total != 6 {
		t.Errorf("expected 6 received %v", total)
	}
}
