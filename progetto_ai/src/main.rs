use rand::Rng;
use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};
use chrono::{DateTime, NaiveDateTime, Utc, Datelike};
use pyo3::prelude::*;
use pyo3::types::PyModule;

static mut MEMORIA: Option<HashMap<String, String>> = None;

fn main() {
    // Inizializza l'interprete Python per PyO3
    pyo3::prepare_freethreaded_python();

    unsafe {
        if MEMORIA.is_none() {
            MEMORIA = Some(HashMap::new());
        }
    }

    // Codice esistente
    println!("Hello, world!");
    println!("{}", consiglia());

    // Codice di crittografia
    let messaggio = "Ciao amore, messaggio segreto!";
    let password = "super_segreta_password";

    Python::with_gil(|py| {
        let security = PyModule::from_code_bound(py, include_str!("security.py"), "security.py", "security")
            .expect("Errore nel caricamento di security.py");

        // Crittografia
        let messaggio_criptato: String = security
            .call_method1("encrypt_message", (messaggio, password))
            .unwrap()
            .extract()
            .unwrap();
        println!("Messaggio criptato: {}", messaggio_criptato);

        // Decriptazione
        let messaggio_decriptato: String = security
            .call_method1("decrypt_message", (messaggio_criptato.clone(), password))
            .unwrap()
            .extract()
            .unwrap();
        println!("Messaggio decriptato: {}", messaggio_decriptato);
    });

    // Altre funzionalità
    println!("Somma di 5 e 3: {}", somma(5, 3));
    println!("Differenza tra 5 e 3: {}", sottrai(5, 3));
    println!("Moltiplicazione di 5 e 3: {}", moltiplica(5, 3));
    println!("Divisione di 6 per 3: {}", dividi(6, 3));

    let frase = "Questa è una frase di esempio";
    println!("Numero di parole: {}", conta_parole(frase));

    println!("Data e ora corrente: {}", data_ora_corrente());

    ricorda("nome", "Alessandro");
    println!("Recupero nome: {}", recupera("nome"));

    println!("Risposta alla domanda 'Come stai?': {}", rispondi("Come stai?"));
    println!("La tua età è: {} anni", calcola_eta(1990));
    println!("Numero casuale tra 1 e 6 (simulazione dado): {}", genera_numero_casuale(1, 6));

    println!("Imposto un promemoria: {}", imposta_promemoria("Prendere le medicine alle 18"));
    println!("Comando di sistema 'Alza il volume': {}", comando_sistema("Alza il volume"));
    println!("Risposta a domanda complessa: {}", domanda_complessa("Calcola 10 diviso 2"));
}

fn consiglia() -> &'static str {
    let consigli = ["Continua così!", "Non mollare!", "Sei un campione!"];
    let mut rng = rand::thread_rng();
    consigli[rng.gen_range(0..consigli.len())]
}

fn somma(a: i32, b: i32) -> i32 { a + b }
fn sottrai(a: i32, b: i32) -> i32 { a - b }
fn moltiplica(a: i32, b: i32) -> i32 { a * b }
fn dividi(a: i32, b: i32) -> i32 { a / b }

fn conta_parole(frase: &str) -> usize {
    frase.split_whitespace().count()
}

fn data_ora_corrente() -> String {
    let start = SystemTime::now();
    let since_the_epoch = start.duration_since(UNIX_EPOCH).expect("Errore nel calcolo del tempo");
    let datetime = NaiveDateTime::from_timestamp(since_the_epoch.as_secs() as i64, 0);
    DateTime::<Utc>::from_utc(datetime, Utc).format("%Y-%m-%d %H:%M:%S").to_string()
}

fn ricorda(chiave: &str, valore: &str) {
    unsafe {
        if let Some(ref mut memoria) = MEMORIA {
            memoria.insert(chiave.to_string(), valore.to_string());
        }
    }
}

fn recupera(chiave: &str) -> String {
    unsafe {
        if let Some(ref memoria) = MEMORIA {
            memoria.get(chiave).cloned().unwrap_or("Non trovato".to_string())
        } else {
            "Memoria non inizializzata.".to_string()
        }
    }
}

fn rispondi(domanda: &str) -> &'static str {
    match domanda {
        "Come stai?" => "Sto bene, grazie!",
        "Qual è il tuo scopo?" => "Il mio scopo è aiutarti.",
        "Che tempo fa oggi?" => "Oggi è una giornata soleggiata.",
        "Alza il volume" => "Volume alzato!",
        "Dimmi una barzelletta" => "Perché l’uva non ride? Perché si è trasformata in vino!",
        _ => "Mi dispiace, non so come rispondere a questa domanda.",
    }
}

fn calcola_eta(anno_nascita: i32) -> i32 {
    let anno_corrente = Utc::now().year();
    anno_corrente - anno_nascita
}

fn genera_numero_casuale(min: i32, max: i32) -> i32 {
    let mut rng = rand::thread_rng();
    rng.gen_range(min..=max)
}

fn imposta_promemoria(promemoria: &str) -> &'static str {
    println!("Promemoria impostato: {}", promemoria);
    "Promemoria salvato!"
}

fn comando_sistema(comando: &str) -> &'static str {
    match comando {
        "Alza il volume" => "Volume alzato!",
        "Abbassa il volume" => "Volume abbassato!",
        "Accendi la torcia" => "Torcia accesa!",
        "Spegni la torcia" => "Torcia spenta!",
        _ => "Comando non riconosciuto.",
    }
}

fn domanda_complessa(domanda: &str) -> String {
    if domanda.contains("Calcola") && domanda.contains("diviso") {
        let parts: Vec<&str> = domanda.split_whitespace().collect();
        let a: i32 = parts[1].parse().unwrap_or(0);
        let b: i32 = parts[3].parse().unwrap_or(1);
        format!("Il risultato di {} diviso {} è: {}", a, b, a / b)
    } else {
        "Non so come rispondere a questa domanda complessa.".to_string()
    }
}
