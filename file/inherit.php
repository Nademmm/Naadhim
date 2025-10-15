<?php
// Class Induk
class Hewan {
    public $nama;

    public function __construct($nama) {
        $this->nama = $nama;
    }

    public function suara() {
        echo "$this->nama membuat suara umum.\n";
    }
}

// Class Turunan
class Kucing extends Hewan {
    public function suara() {
        echo "$this->nama mengeong: Meong...!\n";
    }
}

class Anjing extends Hewan {
    public function suara() {
        echo "$this->nama menggonggong: Guk guk...!\n";
    }
}

// Penggunaan
$kucing = new Kucing("Kucing");
$kucing->suara();

$anjing = new Anjing("Anjing");
$anjing->suara();
?>


<?php
// Tanpa Inheritance
class Mobil {
    public $merk;

    public function __construct($merk) {
        $this->merk = $merk;
    }

    public function jalan() {
        echo "Mobil $this->merk sedang berjalan.\n";
    }
}

class Motor {
    public $merk;

    public function __construct($merk) {
        $this->merk = $merk;
    }

    public function jalan() {
        echo "Motor $this->merk sedang berjalan.\n";
    }
}

// Penggunaan
$mobil = new Mobil("Toyota");
$mobil->jalan();

$motor = new Motor("Honda");
$motor->jalan();
?>


<?php
// Dengan Inheritance
// Class Induk
class Kendaraan {
    public $merk;

    public function __construct($merk) {
        $this->merk = $merk;
    }

    public function jalan() {
        echo "$this->merk sedang berjalan di jalan raya.\n";
    }
}

// Class Turunan
class Mobil extends Kendaraan {
    public function klakson() {
        echo "Mobil $this->merk membunyikan klakson: Beep Beep!\n";
    }
}

class Motor extends Kendaraan {
    public function klakson() {
        echo "Motor $this->merk membunyikan klakson: Tiiin Tiiin!\n";
    }
}

// Penggunaan
$mobil = new Mobil("Toyota");
$mobil->jalan();    
$mobil->klakson();  

$motor = new Motor("Honda");
$motor->jalan();    
$motor->klakson();  
?>

