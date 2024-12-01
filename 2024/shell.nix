{pkgs ? import <nixpkgs> {}}:
pkgs.mkShellNoCC {
  packages = [
    (
      pkgs.python3.withPackages (python-pkgs: [
        python-pkgs.debugpy
      ])
    )
  ];
}
